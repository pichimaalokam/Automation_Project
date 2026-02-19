from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    assert inventory.get_cart_count() == "1"