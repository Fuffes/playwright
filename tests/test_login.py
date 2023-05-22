import asyncio

import pytest
from playwright.async_api import Playwright, Page, expect
from pages.Login import LoginPage
from configuration import URL_PRODUCT, URL_BASE, VALID_LOGINS, INVALID_LOGINS
from pages.Products import ProductPage

@pytest.mark.parametrize(
    'valid_login', VALID_LOGINS

)
def test_valid_login(page, valid_login):

    login_page = LoginPage(page)
    login_page.navigate(URL_BASE)
    login_page.enter_login(valid_login)
    login_page.enter_password()
    login_page.press_btn()

    if page.is_disabled(login_page.error_message):
        print('error') # assert login_page.errorMess_equal_to('Epic sadface: Username and password do not match any user in this service')

    else: print('else') #  assert page.url==URL_PRODUCT

