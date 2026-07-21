from pages.base_page import BasePage
from config.settings import BASE_URL, TIMEOUT

class HomePage(BasePage):
    SIGNUP_LOGIN_BTN = "a[href='/login']"
    LOGGED_IN_USER = "a:has-text('Logged in as')"
    PRODUCTS_BTN = "a[href='/products']"
    CART_BTN = "a[href='/view_cart']"
    CONTACT_US_BTN = "a[href='/contact_us']"
    TEST_CASES_BTN = "a[href='/test_cases']"
    HOME_PAGE_LOGO = "img[alt='Website for automation practice']"
    FOOTER_SUBSCRIPTION_TEXT = "h2:has-text('Subscription')"
    SUBSCRIPTION_EMAIL_INPUT = "#susbscribe_email"
    SUBSCRIPTION_BUTTON = "#subscribe"
    SUBSCRIPTION_SUCCESS = "#success-subscribe"
    ARROW_UP_BUTTON = "#scrollUp"
    FULL_FLEGED_TEXT = "h2:has-text('Full-Fledged practice website')"

    def navigate_to_home(self):
        self.navigate(BASE_URL)
        self.accept_consent()

    def is_home_visible(self):
        return self.is_visible(self.HOME_PAGE_LOGO)

    def click_signup_login(self):
        # Utilise le rôle "link" pour éviter l'ambiguïté
        self.page.get_by_role("link", name="Signup / Login").click(timeout=TIMEOUT)

    def click_products(self):
        # Force le clic même si une pub intercepte
        self.page.locator(self.PRODUCTS_BTN).first.click(force=True, timeout=TIMEOUT)

    def click_cart(self):
        self.page.locator(self.CART_BTN).first.click(force=True, timeout=TIMEOUT)

    def click_contact_us(self):
        self.click(self.CONTACT_US_BTN)

    def click_test_cases(self):
        self.page.locator(self.TEST_CASES_BTN).first.click(force=True, timeout=TIMEOUT)

    def get_logged_in_user_text(self):
        return self.get_text(self.LOGGED_IN_USER)

    def scroll_down_to_footer(self):
        self.scroll_to_bottom()

    def verify_subscription_text(self):
        return self.is_visible(self.FOOTER_SUBSCRIPTION_TEXT)

    def fill_subscription_email(self, email):
        self.fill(self.SUBSCRIPTION_EMAIL_INPUT, email)

    def click_subscription_arrow(self):
        self.click(self.SUBSCRIPTION_BUTTON)

    def get_subscription_success_text(self):
        return self.get_text(self.SUBSCRIPTION_SUCCESS)

    def click_arrow_up(self):
        self.click(self.ARROW_UP_BUTTON)

    def is_full_fledged_text_visible(self):
        return self.page.locator(self.FULL_FLEGED_TEXT).first.is_visible()
