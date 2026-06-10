from pages.base_page import BasePage

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
        self.page.wait_for_selector("#cart_info_table", state="attached", timeout=10000)
        rows = self.page.locator("#cart_info_table tbody tr")
        return rows.count()

    def click_proceed_to_checkout(self):
        self.page.locator(self.PROCEED_TO_CHECKOUT_BTN).first.click(force=True)

    def click_register_login_from_checkout(self):
        self.click(self.REGISTER_LOGIN_LINK)

    def get_product_quantity(self, index=0):
        return self.page.locator(self.PRODUCT_QUANTITY).nth(index).text_content().strip()

    def remove_first_product(self):
        self.page.locator(self.REMOVE_PRODUCT_BTN).first.click()
