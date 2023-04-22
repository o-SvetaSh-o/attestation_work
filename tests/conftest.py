import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    """ Фикстура запуска браузера

    :return:
    """

    driver = webdriver.Chrome('../chromedriver.exe')
    yield driver

    driver.quit()