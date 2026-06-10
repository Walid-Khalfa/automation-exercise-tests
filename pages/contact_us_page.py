from pages.base_page import BasePage

class ContactUsPage(BasePage):
    GET_IN_TOUCH_HEADER = "h2:has-text('Get In Touch')"
    NAME_INPUT = "input[data-qa='name']"
    EMAIL_INPUT = "input[data-qa='email']"
    SUBJECT_INPUT = "input[data-qa='subject']"
    MESSAGE_TEXTAREA = "textarea[data-qa='message']"
    UPLOAD_FILE_INPUT = "input[name='upload_file']"
    SUBMIT_BTN = "input[data-qa='submit-button']"
    SUCCESS_MESSAGE = ".alert-success"
    HOME_BTN = "a:has-text('Home')"

    def is_get_in_touch_visible(self):
        return self.is_visible(self.GET_IN_TOUCH_HEADER)

    def fill_contact_form(self, name, email, subject, message):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.SUBJECT_INPUT, subject)
        self.fill(self.MESSAGE_TEXTAREA, message)

    def upload_file(self, file_path):
        self.page.set_input_files(self.UPLOAD_FILE_INPUT, file_path)

    def click_submit(self):
        # Gérer la boîte de dialogue JavaScript
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.click(self.SUBMIT_BTN)

    def get_success_message(self):
        success = self.page.locator(self.SUCCESS_MESSAGE).first
        success.wait_for(state="visible", timeout=15000)
        return success.inner_text()

    def click_home(self):
        self.page.locator(self.HOME_BTN).first.click()
