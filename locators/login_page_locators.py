from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, ".//input[@name='name']")
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    