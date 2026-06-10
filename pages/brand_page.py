from pages.base_page import BasePage

class BrandPage(BasePage):
    BRANDS_SIDEBAR = ".brands_products"
    POLO_BRAND = "a:has-text('Polo')"
    BABYHUG_BRAND = "a:has-text('Babyhug')"
    BRAND_PRODUCTS_HEADER = "h2.title"

    def is_brands_visible(self):
        self.page.wait_for_selector(self.BRANDS_SIDEBAR, timeout=10000)
        self.page.locator(self.BRANDS_SIDEBAR).scroll_into_view_if_needed()
        return self.is_visible(self.BRANDS_SIDEBAR)

    def click_polo_brand(self):
        # Forcer le clic pour éviter les publicités
        self.page.locator(self.POLO_BRAND).first.click(force=True)

    def click_babyhug_brand(self):
        self.page.locator(self.BABYHUG_BRAND).first.click(force=True)

    def get_brand_header_text(self):
        return self.page.locator(self.BRAND_PRODUCTS_HEADER).first.inner_text()
