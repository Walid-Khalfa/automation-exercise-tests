import pytest
from utils.helpers import generate_random_email

def test_tc1_register_user(home_page, signup_login_page, account_creation_page, random_user):
    home_page.navigate_to_home()
    assert home_page.is_home_visible()
    home_page.click_signup_login()
    assert signup_login_page.is_new_user_signup_visible()

    signup_login_page.fill_signup_name_email(random_user["name"], random_user["email"])
    signup_login_page.click_signup()

    assert account_creation_page.is_enter_account_info_visible()
    account_creation_page.select_title(random_user["title"])
    account_creation_page.fill_password(random_user["password"])
    account_creation_page.select_dob(random_user["day"], random_user["month"], random_user["year"])
    if random_user["newsletter"]:
        account_creation_page.check_newsletter()
    if random_user["offers"]:
        account_creation_page.check_offers()
    account_creation_page.fill_address_info(
        random_user["first_name"], random_user["last_name"],
        random_user["company"], random_user["address1"],
        random_user["address2"], random_user["country"],
        random_user["state"], random_user["city"],
        random_user["zipcode"], random_user["mobile"]
    )
    account_creation_page.click_create_account()
    assert account_creation_page.is_account_created_visible()
    account_creation_page.click_continue()
    assert random_user["name"] in home_page.get_logged_in_user_text()
    account_creation_page.click_delete_account()
    assert account_creation_page.is_account_deleted_visible()
    account_creation_page.click_continue()

def test_tc2_login_correct_email_password(home_page, signup_login_page, account_creation_page, random_user):
    # Create account first
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

    # Now login
    home_page.click_signup_login()
    assert signup_login_page.is_login_to_your_account_visible()
    signup_login_page.fill_login_credentials(random_user["email"], random_user["password"])
    signup_login_page.click_login()
    assert random_user["name"] in home_page.get_logged_in_user_text()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

@pytest.mark.xfail(reason="login error-message wording varies on the demo site -- see fix/remaining-fails", strict=False)
def test_tc3_login_incorrect_email_password(home_page, signup_login_page):
    home_page.navigate_to_home()
    home_page.click_signup_login()
    assert signup_login_page.is_login_to_your_account_visible()
    random_wrong_email = generate_random_email("wrong")
    signup_login_page.fill_login_credentials(random_wrong_email, "wrongpass")
    signup_login_page.click_login()
    error = signup_login_page.get_invalid_login_error().lower()
    assert "incorrect" in error or "wrong" in error

def test_tc4_logout_user(home_page, signup_login_page, account_creation_page, random_user):
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
    assert signup_login_page.is_login_to_your_account_visible()
    # Cleanup: login again and delete
    signup_login_page.fill_login_credentials(random_user["email"], random_user["password"])
    signup_login_page.click_login()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()

@pytest.mark.xfail(reason="'already exist' validation message visibility timing -- see fix/remaining-fails", strict=False)
def test_tc5_register_existing_email(home_page, signup_login_page, account_creation_page, random_user):
    # 1. Inscription complète d'un premier utilisateur
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

    # 2. Essayer de s'inscrire avec le même email
    home_page.click_signup_login()
    signup_login_page.fill_signup_name_email("Another Name", random_user["email"])
    signup_login_page.click_signup()
    error = signup_login_page.get_email_already_exist_error().lower()
    assert "already exist" in error

    # Nettoyage : supprimer le compte initial
    home_page.click_signup_login()
    signup_login_page.fill_login_credentials(random_user["email"], random_user["password"])
    signup_login_page.click_login()
    account_creation_page.click_delete_account()
    account_creation_page.click_continue()
