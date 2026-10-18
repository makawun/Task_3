import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data.urls import Urls


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        super().open(Urls.LOGIN)
        self.wait_url_contains(Urls.LOGIN)

    @allure.step("Войти: {email}")
    def login(self, email: str, password: str):
        self.send_keys(LoginPageLocators.EMAIL, email)
        self.send_keys(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_url_not_contains(Urls.LOGIN)

    @allure.step("Клик по ссылке «Восстановить пароль»")
    def click_password_recovery(self):
        self.click(LoginPageLocators.PASSWORD_RECOVERY_LINK)
        self.wait_url_contains(Urls.FORGOT_PASSWORD)
        
        