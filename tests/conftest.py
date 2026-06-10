import os
from pathlib import Path

import pytest

# Skip tests at collection if Playwright browsers are not installed
_playwright_browsers_path = Path(os.path.expanduser("~/.cache/ms-playwright"))
if not _playwright_browsers_path.exists():
    pytest.skip(
        "Playwright browsers not installed. Run 'python -m playwright install' to install browsers.",
        allow_module_level=True,
    )

from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.category_page import CategoryPage
from pages.brand_page import BrandPage
from utils.helpers import generate_random_user_data
from utils.data_loader import load_json

@pytest.fixture(scope="function")
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture(scope="function")
def signup_login_page(page: Page):
    return SignupLoginPage(page)

@pytest.fixture(scope="function")
def account_creation_page(page: Page):
    return AccountCreationPage(page)

@pytest.fixture(scope="function")
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture(scope="function")
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture(scope="function")
def checkout_page(page: Page):
    return CheckoutPage(page)

@pytest.fixture(scope="function")
def contact_us_page(page: Page):
    return ContactUsPage(page)

@pytest.fixture(scope="function")
def test_cases_page(page: Page):
    return TestCasesPage(page)

@pytest.fixture(scope="function")
def category_page(page: Page):
    return CategoryPage(page)

@pytest.fixture(scope="function")
def brand_page(page: Page):
    return BrandPage(page)

@pytest.fixture
def random_user():
    return generate_random_user_data()

@pytest.fixture
def payment_data():
    return load_json("payment_data.json")
