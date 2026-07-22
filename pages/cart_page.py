from pages.base_page import BasePage
from config.settings import TIMEOUT

class CartPage(BasePage):
    CART_PAGE_TEXT = "#cart_info"
    PROCEED_TO_CHECKOUT_BTN = "a:has-text('Proceed To Checkout')"
    REGISTER_LOGIN_LINK = "u:has-text('Register / Login')"
    CART_ITEMS = ".cart_items .cart_product"
    PRODUCT_QUANTITY = ".cart_quantity button"
    PRODUCT_PRICE = ".cart_price"
    PRODUCT_TOTAL = ".cart_total_price"
    REMOVE_PRODUCT_BTN = ".cart_quantity_delete"

    def is_cart_page_displayed(self):
        return self.is_visible(self.CART_PAGE_TEXT)

    def get_cart_items_count(self):
        self.page.wait_for_selector("#cart_info_table", state="attached", timeout=TIMEOUT)
        rows = self.page.locator("#cart_info_table tbody tr")
        return rows.count()

    def click_proceed_to_checkout(self):
        # The cart page occasionally arrives with markup still streaming in,
        # so wait for the button to be visible (cheap fail-fast vs. the full
        # actionability wait inside click()).
        self.page.wait_for_selector(
            self.PROCEED_TO_CHECKOUT_BTN, state="visible", timeout=TIMEOUT
        )
        self.page.locator(self.PROCEED_TO_CHECKOUT_BTN).first.click(force=True, timeout=TIMEOUT)

    def click_register_login_from_checkout(self):
        self.click(self.REGISTER_LOGIN_LINK)

    def get_product_quantity(self, index=0):
        return self.page.locator(self.PRODUCT_QUANTITY).nth(index).text_content(timeout=TIMEOUT).strip()

    def remove_first_product(self):
        self.page.locator(self.REMOVE_PRODUCT_BTN).first.click(timeout=TIMEOUT)
