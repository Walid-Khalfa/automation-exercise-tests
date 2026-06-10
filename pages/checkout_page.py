from pages.base_page import BasePage

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
        pay_btn = self.page.locator(self.PAY_AND_CONFIRM_BTN)
        # Clic forcé, ne pas attendre de navigation (AJAX)
        pay_btn.click(force=True)
        # Attendre que la page de confirmation apparaisse
        self.page.wait_for_timeout(2000)

    def is_order_successful(self):
        try:
            self.page.wait_for_selector("text=Order Placed", timeout=10000)
            return True
        except:
            if "payment_done" in self.page.url or "order_placed" in self.page.url:
                return True
            return False
