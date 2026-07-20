import time

from pages.base_page import BasePage
from config.settings import TIMEOUT

class CheckoutPage(BasePage):
    ADDRESS_DETAILS_SECTION = "#address_delivery"
    REVIEW_ORDER_SECTION = "#cart_info"
    COMMENT_TEXTAREA = ".form-control"
    PLACE_ORDER_BTN = "a:has-text('Place Order')"
    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"
    PAY_AND_CONFIRM_BTN = "button[data-qa='pay-button']"

    def is_address_details_visible(self):
        return self.is_visible(self.ADDRESS_DETAILS_SECTION)

    def fill_comment(self, comment):
        self.fill(self.COMMENT_TEXTAREA, comment)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)

    def fill_payment_details(self, name_on_card, card_number, cvc, month, year):
        self.fill(self.NAME_ON_CARD, name_on_card)
        self.fill(self.CARD_NUMBER, card_number)
        self.fill(self.CVC, cvc)
        self.fill(self.EXPIRY_MONTH, month)
        self.fill(self.EXPIRY_YEAR, year)

    def click_pay_and_confirm(self):
        """Click 'Pay and Confirm Order'. Tolerant of ad/cookie overlay intercepts.

        Tries a proper click first, then falls back to force-click to bypass
        overlays. Does NOT block on a hard sleep -- the caller should rely on
        `is_order_successful()` which polls for the success signals.
        """
        pay_btn = self.page.locator(self.PAY_AND_CONFIRM_BTN)
        try:
            pay_btn.scroll_into_view_if_needed(timeout=5000)
        except Exception:
            pass
        try:
            pay_btn.click(timeout=TIMEOUT)
        except Exception:
            pay_btn.click(force=True)

    def is_order_successful(self):
        """Poll up to TIMEOUT for any of several success signals.

        The demo site's payment AJAX occasionally takes 5-30s to resolve; a
        single-shot `wait_for_selector` is brittle, so we poll a ladder of
        success indicators for up to TIMEOUT ms and return True on the first
        match. False is returned ONLY if no signal fires within the budget.
        """
        # Cap polling at half the global TIMEOUT -- 30s by default. The original
        # code gave up at 10s which was brittle on slow AJAX; 30s is generous
        # without making CI regressions cost 60s+ per failing test.
        deadline = time.monotonic() + (TIMEOUT / 2000)
        success_selectors = [
            "text=Order Placed",
            "text=Your order has been placed",
            "h2:has-text('Order Placed')",
        ]
        while time.monotonic() < deadline:
            url = self.page.url
            if "payment_done" in url or "order_placed" in url or "/order_placed" in url:
                return True
            for sel in success_selectors:
                try:
                    if self.page.locator(sel).first.is_visible():
                        return True
                except Exception:
                    continue
            self.page.wait_for_timeout(500)
        return False
