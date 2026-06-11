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
        # Allow some time for rendering after ads or redirects
        try:
            self.page.locator(self.LOGIN_TO_YOUR_ACCOUNT_TEXT).first.wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    def fill_login_credentials(self, email, password):
        self.page.locator(self.LOGIN_EMAIL).wait_for(state="visible", timeout=10000)
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_invalid_login_error(self):
        error = self.page.get_by_text("Your email or password is incorrect!")
        error.wait_for(state="visible", timeout=10000)
        return error.text_content()

    def get_email_already_exist_error(self):
        error = self.page.locator(".signup-form p", has_text="already exist")
        error.wait_for(state="visible", timeout=10000)
        return error.text_content()
