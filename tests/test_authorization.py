from time import sleep

import pytest

from accounts import VALID_LOGIN, VALID_PASS
from objects.pages.base_page import BasePage
from urls import AUTH_URL, REGISTRATION_URL
from objects.locators.auth_locators import AuthLocators as AL
from objects.locators.profile_locators import ProfileLocators as PL


@pytest.fixture(scope='function')
def open_authorization_url(browser):
    """ Фикстура открытия страницы авторизации"""
    page = BasePage(browser)
    page.go_to_url(AUTH_URL)
    yield browser
    page.go_to_url(AUTH_URL)


class TestAuthorizationPage:

    def test_open_registration_page(self, open_authorization_url):
        """Проверка перехода на страницу регистрации"""

        page = BasePage(open_authorization_url)
        page.clicker(AL.REGISTRATION_BTN)

        assert REGISTRATION_URL in page.get_current_url()

    @pytest.mark.parametrize("links, exp_url", [(AL.VK_REFERENCE_BTN, "https://oauth.vk.com/"),
                                                (AL.OK_REFERENCE_BTN, "https://connect.ok.ru/"),
                                                (AL.MAIL_REFERENCE_BTN, "https://connect.mail.ru/"),
                                                (AL.GOOGLE_REFERENCE_BTN, "https://accounts.google.com/"),
                                                (AL.YANDEX_REFERENCE_BTN, "https://passport.yandex.ru/")])
    def test_check_reference_links(self, open_authorization_url, links, exp_url):
        """Проверка перехода на страницы авторизации через соцсети """

        page = BasePage(open_authorization_url)
        page.clicker(links)
        url = page.get_current_url()
        assert url.startswith(exp_url), f'Url is different.\nUrl: {url}'

    def test_positive_login(self, open_authorization_url):
        """Позитивная проверка авторизации"""

        page = BasePage(open_authorization_url)
        page.send_value(AL.USER_NAME_INPUT, value=VALID_LOGIN)
        page.send_value(AL.PASSWORD_INPUT, value=VALID_PASS)
        page.clicker(AL.LOGIN_BTN)
        assert page.find_element_page(PL.LOGOUT_BTN)

    @pytest.mark.parametrize('login, password', [('', ''),
                                                 (VALID_LOGIN, ''),
                                                 ('', VALID_PASS)])
    def test_negative_login(self, open_authorization_url, login, password):
        """Негатиная проверка авторизации"""
        page = BasePage(open_authorization_url)
        page.send_value(AL.USER_NAME_INPUT, value=login)
        page.send_value(AL.PASSWORD_INPUT, value=password)
        page.clicker(AL.LOGIN_BTN)
        assert page.find_element_page(AL.LOGIN_BTN)
        assert page.get_current_url().startswith(AUTH_URL)


