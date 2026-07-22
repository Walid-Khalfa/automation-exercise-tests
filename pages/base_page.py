from playwright.sync_api import Page
from config.settings import TIMEOUT

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url, retries=2):
        for i in range(retries):
            try:
                self.page.goto(url, timeout=TIMEOUT, wait_until="domcontentloaded")
                return
            except Exception as e:
                if i == retries - 1:
                    raise e
                self.page.wait_for_timeout(2000)

    def accept_consent(self):
        try:
            consent_btn = self.page.locator(".fc-button.fc-cta-consent")
            consent_btn.wait_for(state="visible", timeout=TIMEOUT)
            consent_btn.click()
            self.page.wait_for_timeout(1000)
        except:
            pass

    def click(self, selector: str):
        self.page.locator(selector).first.click(timeout=TIMEOUT)

    def fill(self, selector: str, text: str):
        self.page.locator(selector).first.fill(text, timeout=TIMEOUT)

    def get_text(self, selector: str) -> str:
        # inner_text() already auto-waits up to `timeout` for the locator to
        # become actionable -- no need for an explicit wait_for(state="visible")
        # first (that would have doubled per-fetch wait to 2*TIMEOUT in the
        # worst case).
        return self.page.locator(selector).first.inner_text(timeout=TIMEOUT)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.locator(selector).first.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def wait_for_selector(self, selector: str, timeout=None):
        self.page.wait_for_selector(selector, timeout=timeout)

    def select_option(self, selector: str, value: str):
        self.page.select_option(selector, value)

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.page.mouse.wheel(0, -10000)
        self.page.wait_for_timeout(1000)
