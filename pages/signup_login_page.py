from pages.base_page import BasePage
from config.settings import TIMEOUT

class SignupLoginPage(BasePage):
    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    NEW_USER_SIGNUP_TEXT = "h2:has-text('New User Signup!')"

    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGIN_TO_YOUR_ACCOUNT_TEXT = "h2:has-text('Login to your account')"

    def is_new_user_signup_visible(self):
        return self.is_visible(self.NEW_USER_SIGNUP_TEXT)

    def fill_signup_name_email(self, name, email):
        self.page.locator(self.SIGNUP_NAME).wait_for(state="visible", timeout=10000)
        self.fill(self.SIGNUP_NAME, name)
        self.fill(self.SIGNUP_EMAIL, email)

    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def is_login_to_your_account_visible(self):
        return self.is_visible(self.LOGIN_TO_YOUR_ACCOUNT_TEXT)

    def fill_login_credentials(self, email, password):
        self.page.locator(self.LOGIN_EMAIL).wait_for(state="visible", timeout=10000)
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_invalid_login_error(self):
        """Return the visible login-failure error message, lower-cased.

        The automationexercise.com login form renders the 'wrong credentials'
        notice in several ways across runs (red <p>, .alert, [role=alert], or
        just inline text). We try a selector ladder and treat any of them as
        the canonical message; the test assertion matches a keyword tuple so
        wording drift is tolerated but a missing error still surfaces loudly.
        """
        error_locators = [
            ".login-form p[style*='color: red']",
            ".login-form .alert",
            ".login-form [role='alert']",
            ".login-form .alert-danger",
            ".login-form p:has-text('incorrect')",
            ".login-form p:has-text('wrong')",
            ".login-form p:has-text('invalid')",
        ]
        per_selector_timeout = max(2000, TIMEOUT // max(1, len(error_locators)))
        for loc in error_locators:
            try:
                el = self.page.locator(loc).first
                el.wait_for(state="visible", timeout=per_selector_timeout)
                return (el.text_content() or "").strip().lower()
            except Exception:
                continue
        if "login" in self.page.url:
            raise AssertionError(
                f"Expected an 'incorrect/wrong/invalid credentials' error but none visible. URL={self.page.url}"
            )
        raise AssertionError(
            f"Login likely succeeded (URL no longer /login); the test expected a failure. URL={self.page.url}"
        )

    def get_email_already_exist_error(self):
        """Return the visible duplicate-email error, lower-cased.

        Mirrors the rationale in `get_invalid_login_error`. The signup form
        may render the duplicate-email notice as red <p>, .alert, [role=alert],
        or inline text body. We accept any of those so wording drift on the
        demo site no longer breaks the test.
        """
        error_locators = [
            ".signup-form p[style*='color: red']",
            ".signup-form .alert",
            ".signup-form [role='alert']",
            ".signup-form .alert-danger",
            ".signup-form p:has-text('already exist')",
            ".signup-form p:has-text('registered')",
        ]
        per_selector_timeout = max(2000, TIMEOUT // max(1, len(error_locators)))
        for loc in error_locators:
            try:
                el = self.page.locator(loc).first
                el.wait_for(state="visible", timeout=per_selector_timeout)
                return (el.text_content() or "").strip().lower()
            except Exception:
                continue
        if "/signup" in self.page.url or "/login" in self.page.url:
            raise AssertionError(
                f"Expected a duplicate-email notice but none visible. URL={self.page.url}"
            )
        raise AssertionError(
            f"Signup likely succeeded (URL no longer contains /signup or /login); the test expected a duplicate-email rejection. URL={self.page.url}"
        )
