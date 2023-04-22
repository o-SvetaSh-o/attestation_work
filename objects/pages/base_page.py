from time import sleep

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __int__(self, browser, timeout: int = 15):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.waiting_time = 15

    def wait_for_element_present(self, loc: tuple, waiting_time: int):

        try:
            element = self.browser.WebDriverWait(waiting_time).until(EC.presence_of_element_located(*loc))
            return element
        except:
            raise Exception("")

    def find_element(self, loc):

        try:
            elem = self.wait_for_element_present(*loc, waiting_time=self.waiting_time).find_element()
            return elem
        except:
            raise Exception("")

    def send_value(self, loc, value):

        return self.find_element(*loc).send_keys(value)

    def clicker(self, loc):

        self.find_element(loc).click()

    def go_to_url(self, page_url):

        try:
            before_url = self.browser.current_url

            if before_url == page_url:
                self.browser.get('about:blank')
                sleep(2)
            self.browser.get(page_url)
        except:
            raise Exception("")





