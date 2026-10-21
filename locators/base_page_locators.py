from selenium.webdriver.common.by import By


class BasePageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")
    ORDER_TAPE = (By.XPATH, ".//a[@href='/feed']")
    CONSTRUCTOR = (By.XPATH, ".//li/a[@href='/']")
    MODAL_OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")