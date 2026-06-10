from pages.base_page import BasePage

class CategoryPage(BasePage):
    WOMEN_CATEGORY = "a:has-text('Women')"
    WOMEN_DRESS_SUB = "a:has-text('Dress')"
    MEN_CATEGORY = "a:has-text('Men')"
    MEN_TSHIRTS_SUB = "a:has-text('Tshirts')"
    CATEGORY_PRODUCTS_HEADER = "h2.title"

    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)

    def click_women_dress(self):
        self.page.locator(self.WOMEN_DRESS_SUB).first.click()

    def click_men_category(self):
        self.click(self.MEN_CATEGORY)

    def click_men_tshirts(self):
        self.click(self.MEN_TSHIRTS_SUB)

    def get_category_header_text(self):
        return self.page.locator(self.CATEGORY_PRODUCTS_HEADER).first.inner_text()
