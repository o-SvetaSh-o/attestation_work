from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __int__(self, browser):
        self.browser = browser
        self.waiting_time = 15

    def wait_for_element_present(self, loc, waiting_time: int):

        try:
            element = self.browser.WebDriverWait(waiting_time).until(EC.presence_of_element_located(*loc))
            return element
        except Exception:
            print("Element is absent")

    def find_element(self, loc):

        try:
            elem = self.wait_for_element_present(*loc, waiting_time=self.waiting_time).find_element()
            return elem
        except Exception:
            print("Element is absent")

    def send_value(self, loc, value):

        return self.find_element(*loc).send_keys(value)

    def clicker(self, loc):

        self.find_element(loc).click()