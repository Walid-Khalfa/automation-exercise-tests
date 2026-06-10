import os

def test_tc6_contact_us_form(home_page, contact_us_page):
    home_page.navigate_to_home()
    home_page.click_contact_us()
    assert contact_us_page.is_get_in_touch_visible()
    contact_us_page.fill_contact_form("John Doe", "john@test.com", "Test Subject", "Hello this is a message")
    # Create a dummy file to upload
    try:
        upload_path = "test_upload.txt"
        with open(upload_path, "w") as f:
            f.write("test content")
        contact_us_page.upload_file(upload_path)
        contact_us_page.click_submit()
        assert "submitted successfully" in contact_us_page.get_success_message().lower()
        contact_us_page.click_home()
        assert home_page.is_home_visible()
    finally:
        try:
            if os.path.exists(upload_path):
                os.remove(upload_path)
        except Exception:
            pass

def test_tc10_subscription_in_home_page(home_page):
    home_page.navigate_to_home()
    home_page.scroll_down_to_footer()
    assert home_page.verify_subscription_text()
    home_page.fill_subscription_email("test@example.com")
    home_page.click_subscription_arrow()
    assert "subscribed" in home_page.get_subscription_success_text().lower()

def test_tc11_subscription_in_cart_page(home_page, cart_page):
    home_page.navigate_to_home()
    home_page.click_cart()
    home_page.scroll_down_to_footer()
    assert home_page.verify_subscription_text()
    home_page.fill_subscription_email("carttest@example.com")
    home_page.click_subscription_arrow()
    assert "subscribed" in home_page.get_subscription_success_text().lower()
