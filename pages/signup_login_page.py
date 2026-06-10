from pages.base_page import BasePage

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
        # Le message d'erreur peut être dans un p avec style rouge ou texte exact
        error_locators = [
            "p:has-text('Your email or password is incorrect!')",
            ".login-form p[style*='color: red']",
            ".login-form p:has-text('incorrect')"
        ]
        for loc in error_locators:
            try:
                error = self.page.locator(loc).first
                error.wait_for(state="visible", timeout=5000)
                return error.text_content()
            except:
                continue
        raise Exception("Aucun message d'erreur trouvé")

    def get_email_already_exist_error(self):
        error_locators = [
            "p:has-text('Email Address already exist!')",
            ".signup-form p[style*='color: red']",
            ".signup-form p:has-text('already exist')"
        ]
        for loc in error_locators:
            try:
                error = self.page.locator(loc).first
                error.wait_for(state="visible", timeout=5000)
                return error.text_content()
            except:
                continue
        raise Exception("Aucun message d'erreur trouvé")
