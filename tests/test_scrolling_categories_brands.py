def test_tc18_view_category_products(home_page, category_page):
    home_page.navigate_to_home()
    category_page.click_women_category()
    category_page.click_women_dress()
    assert "WOMEN - DRESS PRODUCTS" in category_page.get_category_header_text().upper()

def test_tc19_view_brand_products(home_page, brand_page):
    home_page.navigate_to_home()
    home_page.click_products()
    assert brand_page.is_brands_visible()
    brand_page.click_polo_brand()
    assert "BRAND - POLO PRODUCTS" in brand_page.get_brand_header_text().upper()
    brand_page.click_babyhug_brand()
    assert "BRAND - BABYHUG PRODUCTS" in brand_page.get_brand_header_text().upper()

def test_tc25_scroll_up_using_arrow_button(home_page):
    home_page.navigate_to_home()
    home_page.scroll_down_to_footer()
    assert home_page.verify_subscription_text()
    home_page.click_arrow_up()
    assert home_page.is_full_fledged_text_visible()

def test_tc26_scroll_up_without_arrow_button(home_page):
    home_page.navigate_to_home()
    home_page.scroll_down_to_footer()
    assert home_page.verify_subscription_text()
    home_page.scroll_to_top()
    assert home_page.is_full_fledged_text_visible()
