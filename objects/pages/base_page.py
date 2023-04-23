from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, timeout: int = 15):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.waiting_time = 15

    def find_element_page(self, *loc, waiting_time=15):
        """
        Метод нахождения элемента на странице
        :param loc: tuple
        :param waiting_time: int
        :return: element
        """
        try:
            element = WebDriverWait(self.browser, waiting_time).until(EC.presence_of_element_located(*loc))
            return element
        except:
            raise Exception("Element is absent!")

    def send_value(self, *loc, value):
        """
        Метод заполнения поля
        :param loc: tuple
        :param value: str
        :return:
        """
        return self.find_element_page(*loc).send_keys(value)

    def clicker(self, *loc):
        """
        Метод нажатия на кнопку
        :param loc: tuple
        :return:
        """
        self.find_element_page(*loc).click()

    def go_to_url(self, page_url):
        """
        Метод перехода по url
        :param page_url: str
        :return:
        """
        try:
            before_url = self.browser.current_url

            if before_url == page_url:
                self.browser.get('about:blank')
                sleep(2)
            self.browser.get(page_url)
        except:
            raise Exception("")

    def get_current_url(self):
        """
        Метод получения текущего url
        :return: str
        """
        sleep(0.2)
        url = self.browser.current_url
        return url

    def get_attributes(self, *loc, attribute: str):
        """Метод получения аттрибутов элемента

        :param loc: tuple
        :param attribute: str
        :return: str
        """

        element = self.find_element_page(*loc)
        if element:
            return element.get_attribute(attribute)





