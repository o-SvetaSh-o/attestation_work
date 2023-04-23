from selenium.webdriver.common.by import By


class AuthLocators:

    REGISTRATION_BTN = (By.XPATH, "//a[@id='kc-register']")
    LOGIN_BTN = (By.XPATH, "//button[@id='kc-login']")
    USER_NAME_INPUT = (By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[   @id='password']")
    VK_REFERENCE_BTN = (By.XPATH, "//a[@id='oidc_vk']")
    OK_REFERENCE_BTN = (By.XPATH, "//a[@id='oidc_ok']")
    MAIL_REFERENCE_BTN = (By.XPATH, "//a[@id='oidc_mail']")
    GOOGLE_REFERENCE_BTN = (By.XPATH, "//a[@id='oidc_google']")
    YANDEX_REFERENCE_BTN = (By.XPATH, "//a[@id='oidc_ya']")
