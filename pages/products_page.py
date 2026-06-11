from pages.base_page import BasePage

class ProductsPage(BasePage):
    ALL_PRODUCTS_HEADER = "h2:has-text('All Products')"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCHED_PRODUCTS_HEADER = "h2:has-text('Searched Products')"
    PRODUCT_LIST = ".product-image-wrapper"
    VIEW_PRODUCT_BTN = "a:has-text('View Product')"
    PRODUCT_NAME = ".product-details h2"
    ADD_TO_CART_BTN = ".add-to-cart"
    CONTINUE_SHOPPING_BTN = "button:has-text('Continue Shopping')"
    VIEW_CART_LINK = "u:has-text('View Cart')"
    RECOMMENDED_ITEMS_SECTION = ".recommended_items"
    ADD_TO_CART_RECOMMENDED = ".recommended_items .add-to-cart"

    def is_all_products_visible(self):
        return self.is_visible(self.ALL_PRODUCTS_HEADER)

    def search_product(self, product_name):
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_searched_products_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_HEADER)

    def get_all_products_elements(self):
        return self.page.locator(self.PRODUCT_LIST).all()

    def click_view_product_of_first(self):
        self.page.locator(self.VIEW_PRODUCT_BTN).first.click()

    def _add_to_cart_from_list(self, index=0):
        self.page.wait_for_selector(self.PRODUCT_LIST, state="visible", timeout=15000)
        products = self.page.locator(self.PRODUCT_LIST)
        product = products.nth(index)
        product.scroll_into_view_if_needed()
        product.wait_for(state="visible", timeout=5000)
        self.page.wait_for_timeout(500)
        product.hover(force=True)
        self.page.wait_for_timeout(500)
        product.locator(self.ADD_TO_CART_BTN).first.click(force=True)
        self.page.wait_for_selector(".modal-content:visible", timeout=15000)

    def add_first_product_to_cart(self):
        if "/product_details/" in self.page.url:
            self.page.locator("button.cart").click(force=True)
        else:
            self._add_to_cart_from_list(0)

    def add_second_product_to_cart(self):
        self._add_to_cart_from_list(1)

    def click_continue_shopping(self):
        self.page.wait_for_selector(".modal-content:visible", timeout=5000)
        self.page.locator("button:has-text('Continue Shopping')").click(force=True)
        self.page.wait_for_selector(".modal-content", state="hidden")

    def click_view_cart(self):
        self.click(self.VIEW_CART_LINK)

    def is_recommended_items_visible(self):
        return self.is_visible(self.RECOMMENDED_ITEMS_SECTION)

    def add_to_cart_from_recommended(self):
        section = self.page.locator(self.RECOMMENDED_ITEMS_SECTION).first
        section.scroll_into_view_if_needed()
        self.page.wait_for_timeout(1000)
        # Hover sur le premier produit de la section
        first_product = section.locator(".product-image-wrapper").first
        first_product.hover()
        self.page.wait_for_timeout(500)
        # Maintenant le bouton est visible
        add_btn = first_product.locator("a.add-to-cart, button:has-text('Add to cart')").first
        add_btn.click(force=True)
        self.page.wait_for_selector(".modal-content:visible", timeout=10000)

    def increase_quantity(self, quantity: int):
        quantity_input = self.page.locator("#quantity")
        quantity_input.fill(str(quantity))
