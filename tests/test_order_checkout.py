import pytest

def test_tc14_place_order_register_while_checkout(home_page, products_page, cart_page, checkout_page, signup_login_page, account_creation_page, random_user, payment_data):
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    cart_page.click_proceed_to_checkout()
    cart_page.click_register_login_from_checkout()

    # Register
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

    # Go to cart and checkout
    home_page.click_cart()
    cart_page.click_proceed_to_checkout()
    assert checkout_page.is_address_details_visible()
    checkout_page.fill_comment("Test order")
    checkout_page.click_place_order()
    checkout_page.fill_payment_details(
        payment_data["name_on_card"], payment_data["card_number"],
        payment_data["cvc"], payment_data["expiry_month"], payment_data["expiry_year"]
    )
    checkout_page.click_pay_and_confirm()
    assert checkout_page.is_order_successful()

    # Cleanup
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

def test_tc15_place_order_register_before_checkout(home_page, products_page, cart_page, checkout_page, signup_login_page, account_creation_page, random_user, payment_data):
    # Register first
    home_page.navigate_to_home()
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

    # Add products and checkout
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    cart_page.click_proceed_to_checkout()
    checkout_page.fill_comment("Order before checkout")
    checkout_page.click_place_order()
    checkout_page.fill_payment_details(
        payment_data["name_on_card"], payment_data["card_number"],
        payment_data["cvc"], payment_data["expiry_month"], payment_data["expiry_year"]
    )
    checkout_page.click_pay_and_confirm()
    assert checkout_page.is_order_successful()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

def test_tc16_place_order_login_before_checkout(home_page, products_page, cart_page, checkout_page, signup_login_page, account_creation_page, random_user, payment_data):
    # Register and login
    home_page.navigate_to_home()
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
    account_creation_page.click_logout()

    # Login again
    home_page.click_signup_login()
    signup_login_page.fill_login_credentials(random_user["email"], random_user["password"])
    signup_login_page.click_login()

    # Add to cart and checkout
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    cart_page.click_proceed_to_checkout()
    checkout_page.fill_comment("Login before checkout")
    checkout_page.click_place_order()
    checkout_page.fill_payment_details(
        payment_data["name_on_card"], payment_data["card_number"],
        payment_data["cvc"], payment_data["expiry_month"], payment_data["expiry_year"]
    )
    checkout_page.click_pay_and_confirm()
    assert checkout_page.is_order_successful()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

def test_tc23_verify_address_details_in_checkout(home_page, products_page, cart_page, checkout_page, signup_login_page, account_creation_page, random_user):
    home_page.navigate_to_home()
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

    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    cart_page.click_proceed_to_checkout()
    assert random_user["address1"] in checkout_page.page.locator("#address_delivery").inner_text()
    assert random_user["city"] in checkout_page.page.locator("#address_delivery").inner_text()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

def test_tc24_download_invoice_after_purchase_order(home_page, products_page, cart_page, checkout_page, signup_login_page, account_creation_page, random_user, payment_data):
    # Similar to TC14, but after order click Download Invoice
    home_page.navigate_to_home()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart()
    cart_page.click_proceed_to_checkout()
    cart_page.click_register_login_from_checkout()
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
    cart_page.click_proceed_to_checkout()
    checkout_page.fill_comment("Test invoice")
    checkout_page.click_place_order()
    checkout_page.fill_payment_details(
        payment_data["name_on_card"], payment_data["card_number"],
        payment_data["cvc"], payment_data["expiry_month"], payment_data["expiry_year"]
    )
    checkout_page.click_pay_and_confirm()
    assert checkout_page.is_order_successful()
    # Click Download Invoice button
    download_btn = home_page.page.locator("a:has-text('Download Invoice')")
    assert download_btn.is_visible()
    download_btn.click()
    # Optionally verify file downloaded
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()
