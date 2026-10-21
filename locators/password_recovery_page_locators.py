from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    EMAIL = (By.XPATH, ".//input[@name='name']")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    # Поле пароля на странице /reset-password
    NEW_PASSWORD = (By.XPATH, ".//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_ICON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    