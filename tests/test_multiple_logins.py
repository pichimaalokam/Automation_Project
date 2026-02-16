import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce"), ("problem_user", "secret_sauce")])

def test_multiple_logins(driver, username, password):

    login = LoginPage(driver)

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if username == "locked_out_user":
        assert "Epic sadface" in driver.page_source
    else:
        assert "inventory" in driver.current_url