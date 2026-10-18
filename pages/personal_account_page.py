import allure

from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.login_page_locators import LoginPageLocators
from data.urls import Urls


class PersonalAccountPage(BasePage):
    @allure.step("Клик по «История заказов»")
    def click_orders_history(self):
        self.click(PersonalAccountPageLocators.ORDERS_HISTORY)
        self.wait_url_contains(Urls.ACCOUNT_ORDER_HISTORY)

    @allure.step("Выйти из аккаунта")
    def click_quit(self):
        self.click(PersonalAccountPageLocators.QUIT_BUTTON)
        self.wait_url_contains(Urls.LOGIN)

    @allure.step("Проверить, что мы на странице входа")
    def is_login_page(self) -> bool:
        return self.find_visible(LoginPageLocators.LOGIN_BUTTON).is_displayed()
    