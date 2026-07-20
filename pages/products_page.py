import time

from pages.base_page import BasePage
from config.settings import TIMEOUT

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
        self.page.locator(self.VIEW_PRODUCT_BTN).first.click(timeout=TIMEOUT)

    def _add_to_cart_from_list(self, index=0):
        product = self.page.locator(self.PRODUCT_LIST).nth(index)
        product.hover()
        self.page.wait_for_timeout(500)
        product.locator(self.ADD_TO_CART_BTN).first.click(force=True)
        self.page.wait_for_selector(".modal-content:visible", timeout=TIMEOUT)

    def add_first_product_to_cart(self):
        if "/product_details/" in self.page.url:
            self.page.locator("button.cart").click(force=True)
        else:
            self._add_to_cart_from_list(0)

    def add_second_product_to_cart(self):
        self._add_to_cart_from_list(1)

    def click_continue_shopping(self):
        self.page.wait_for_selector(".modal-content:visible", timeout=TIMEOUT)
        self.page.locator("button:has-text('Continue Shopping')").click(force=True, timeout=TIMEOUT)
        self.page.wait_for_selector(".modal-content", state="hidden", timeout=TIMEOUT)

    def click_view_cart(self):
        self.click(self.VIEW_CART_LINK)
        # The "View Cart" link inside the added-to-cart modal navigates to
        # /view_cart, but the round-trip can race with the test (especially
        # when an ad iframe intercepts the click). Wait for the cart page
        # URL to surface so the next action reads #cart_info_table against
        # the real /view_cart DOM, not the stale products DOM.
        self.page.wait_for_url("**/view_cart*", timeout=TIMEOUT)

    def is_recommended_items_visible(self):
        return self.is_visible(self.RECOMMENDED_ITEMS_SECTION)

    def add_to_cart_from_recommended(self):
        """Click the first Add-to-Cart button inside the Recommended Items carousel.

        The recommended-products carousel markup varies between demo-site renders
        (different ad-vs-product variants expose the button via different
        selectors). We (a) hover the first product wrapper so the in-image
        overlay appears, then (b) try a selector ladder covering both the
        overlay and the always-on buttons. The follow-up modal is expected,
        but we tolerate the demo site sometimes redirecting directly to
        /view_cart with no modal.
        """
        section = self.page.locator(self.RECOMMENDED_ITEMS_SECTION).first
        try:
            section.scroll_into_view_if_needed(timeout=TIMEOUT)
        except Exception:
            pass
        self.page.wait_for_timeout(500)

        # Hover the first product wrapper (may reveal the in-image "Add to cart" overlay)
        first_product_selectors = [
            ".recommended_items .product-image-wrapper",
            ".recommended_items .item",
            ".recommended_items > div > div",
            ".recommended_items > div",
        ]
        first_product = None
        for sel in first_product_selectors:
            try:
                first_product = self.page.locator(sel).first
                first_product.wait_for(state="attached", timeout=3000)
                break
            except Exception:
                continue
        if first_product is not None:
            try:
                first_product.scroll_into_view_if_needed(timeout=3000)
                first_product.hover()
                self.page.wait_for_timeout(500)
            except Exception:
                pass

        # Now find the Add-to-Cart button. Try the in-product overlay first, then broader.
        add_btn_selectors = [
            ".recommended_items .product-image-wrapper a.add-to-cart",
            ".recommended_items .product-image-wrapper button.cart",
            ".recommended_items button.cart",
            ".recommended_items a.add-to-cart",
            ".recommended_items button:has-text('Add to cart')",
        ]
        add_btn = None
        for sel in add_btn_selectors:
            try:
                add_btn = self.page.locator(sel).first
                add_btn.wait_for(state="visible", timeout=3000)
                break
            except Exception:
                add_btn = None
                continue

        if add_btn is None:
            raise AssertionError(
                "Could not find an Add-to-Cart button inside the Recommended Items section. "
                f"Section visible: {self.is_recommended_items_visible()}; URL={self.page.url}"
            )

        try:
            add_btn.scroll_into_view_if_needed(timeout=3000)
        except Exception:
            pass
        try:
            add_btn.click(timeout=TIMEOUT)
        except Exception:
            add_btn.click(force=True)

        # Modal is expected; tolerate the demo site occasionally navigating directly to /view_cart
        try:
            self.page.wait_for_selector(".modal-content", state="visible", timeout=8000)
        except Exception:
            if "/view_cart" in self.page.url:
                return

    def increase_quantity(self, quantity: int):
        quantity_input = self.page.locator("#quantity")
        quantity_input.fill(str(quantity))
