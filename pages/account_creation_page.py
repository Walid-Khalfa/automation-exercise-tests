from pages.base_page import BasePage

class AccountCreationPage(BasePage):
    ENTER_ACCOUNT_INFO_TEXT = "h2:has-text('Enter Account Information')"
    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"
    PASSWORD = "#password"
    DAYS = "#days"
    MONTHS = "#months"
    YEARS = "#years"
    NEWSLETTER = "#newsletter"
    OFFERS = "#optin"
    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    COMPANY = "#company"
    ADDRESS1 = "#address1"
    ADDRESS2 = "#address2"
    COUNTRY = "#country"
    STATE = "#state"
    CITY = "#city"
    ZIPCODE = "#zipcode"
    MOBILE_NUMBER = "#mobile_number"
    CREATE_ACCOUNT_BTN = "button[data-qa='create-account']"
    ACCOUNT_CREATED_TEXT = "h2[data-qa='account-created'] b"
    CONTINUE_BTN = "a[data-qa='continue-button']"
    ACCOUNT_DELETED_TEXT = "h2[data-qa='account-deleted'] b"
    DELETE_ACCOUNT_BTN = "a[href='/delete_account']"
    LOGOUT_BTN = "a[href='/logout']"

    def is_enter_account_info_visible(self):
        return self.is_visible(self.ENTER_ACCOUNT_INFO_TEXT)

    def select_title(self, title):
        if title.lower() == "mr":
            self.click(self.TITLE_MR)
        else:
            self.click(self.TITLE_MRS)

    def fill_password(self, password):
        self.fill(self.PASSWORD, password)

    def select_dob(self, day, month, year):
        self.select_option(self.DAYS, day)
        self.select_option(self.MONTHS, month)
        self.select_option(self.YEARS, year)

    def check_newsletter(self):
        self.click(self.NEWSLETTER)

    def check_offers(self):
        self.click(self.OFFERS)

    def fill_address_info(self, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.COMPANY, company)
        self.fill(self.ADDRESS1, address1)
        self.fill(self.ADDRESS2, address2)
        self.select_option(self.COUNTRY, country)
        self.fill(self.STATE, state)
        self.fill(self.CITY, city)
        self.fill(self.ZIPCODE, zipcode)
        self.fill(self.MOBILE_NUMBER, mobile)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        self.page.wait_for_url("**/account_created*", timeout=10000)

    def is_account_created_visible(self):
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)

    def click_continue(self):
        # Essayer plusieurs sélecteurs
        selectors = [
            "a[data-qa='continue-button']",
            "a:has-text('Continue')",
            "button:has-text('Continue')",
            ".btn:has-text('Continue')"
        ]
        for selector in selectors:
            try:
                self.page.wait_for_selector(selector, timeout=5000)
                self.page.locator(selector).first.click(force=True)
                return
            except:
                continue
        # Dernier recours : texte exact avec attente explicite
        continue_btn = self.page.get_by_text("Continue", exact=True).first
        continue_btn.wait_for(state="visible", timeout=10000)
        continue_btn.click(force=True)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_BTN)

    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED_TEXT)

    def click_logout(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator("a[href='/logout']").first.click(force=True)
