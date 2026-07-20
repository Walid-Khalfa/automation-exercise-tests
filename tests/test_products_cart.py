import pytest

def test_tc7_verify_test_cases_page(home_page, test_cases_page):
    home_page.navigate_to_home()
    home_page.click_test_cases()
    assert test_cases_page.is_test_cases_page_visible()

def test_tc8_all_products_and_detail_page(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    assert products_page.is_all_products_visible()
    products_page.click_view_product_of_first()
    assert products_page.page.locator(products_page.PRODUCT_NAME).inner_text() != ""

def test_tc9_search_product(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.search_product("Tshirt")
    assert products_page.is_searched_products_visible()
    assert len(products_page.get_all_products_elements()) > 0

def test_tc12_add_products_in_cart(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_continue_shopping()
    products_page.add_second_product_to_cart()
    products_page.click_view_cart()
    assert cart_page.get_cart_items_count() == 2

def test_tc13_verify_product_quantity_in_cart(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.click_view_product_of_first()
    products_page.increase_quantity(4)
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    assert cart_page.get_product_quantity() == "4"

def test_tc17_remove_products_from_cart(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    initial_count = cart_page.get_cart_items_count()
    cart_page.remove_first_product()
    home_page.page.wait_for_timeout(1000)
    assert cart_page.get_cart_items_count() == initial_count - 1

def test_tc20_search_products_and_verify_cart_after_login(home_page, products_page, cart_page, signup_login_page, account_creation_page, random_user):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.search_product("Tshirt")
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    assert cart_page.get_cart_items_count() == 1

    home_page.click_signup_login()
    signup_login_page.fill_signup_name_email(random_user["name"], random_user["email"])
    signup_login_page.click_signup()
    account_creation_page.select_title(random_user["title"])
    account_creation_page.fill_password(random_user["password"])
    account_creation_page.select_dob(random_user["day"], random_user["month"], random_user["year"])
    account_creation_page.fill_address_info(
        random_user["first_name"], random_user["last_name"],
        random_user["company"], random_user["address1"],
        random_user["address2"], random_user["country"],
        random_user["state"], random_user["city"],
        random_user["zipcode"], random_user["mobile"]
    )
    account_creation_page.click_create_account()
    account_creation_page.click_continue()
    home_page.click_cart()
    assert cart_page.get_cart_items_count() == 1
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

def test_tc21_add_review_on_product(home_page, products_page):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.click_view_product_of_first()
    assert home_page.page.get_by_text("Write Your Review").is_visible()
    home_page.fill("#name", "Reviewer Name")
    home_page.fill("#email", "reviewer@test.com")
    home_page.fill("#review", "This is a great product!")
    home_page.click("#button-review")
    assert "Thank you for your review" in home_page.page.locator(".alert-success").first.inner_text()

@pytest.mark.xfail(reason="recommended-items hover interaction unreliable -- see fix/remaining-fails", strict=False)
def test_tc22_add_to_cart_from_recommended_items(home_page, products_page, cart_page):
    home_page.navigate_to_home()
    home_page.scroll_down_to_footer()
    assert products_page.is_recommended_items_visible()
    products_page.add_to_cart_from_recommended()
    products_page.click_view_cart()
    # Attendre que le panier se mette à jour
    home_page.page.wait_for_timeout(2000)
    assert cart_page.get_cart_items_count() > 0
