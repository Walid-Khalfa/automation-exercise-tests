from pages.base_page import BasePage

class TestCasesPage(BasePage):
    TEST_CASES_HEADER = "h2:has-text('Test Cases')"

    def is_test_cases_page_visible(self):
        return self.is_visible(self.TEST_CASES_HEADER)
