import allure

from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from data.texts import Texts, Timeouts
from data.urls import Urls


class PasswordRecoveryPage(BasePage):
    @allure.step("Ввести email для восстановления: {email}")
    def enter_email(self, email: str):
        self.send_keys(PasswordRecoveryPageLocators.EMAIL, email)

    @allure.step("Нажать «Восстановить»")
    def click_recovery(self):
        self.click(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step("Дождаться перехода на страницу сброса пароля")
    def wait_reset_password_page(self, timeout: int = Timeouts.LONG) -> bool:
        return self.wait_url_contains(Urls.RESET_PASSWORD, timeout)

    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_show_password(self):
        self.find_visible(PasswordRecoveryPageLocators.NEW_PASSWORD)
        self.click(PasswordRecoveryPageLocators.SHOW_PASSWORD_ICON)

    @allure.step("Проверить, что поле пароля активно (пароль показан)")
    def is_password_field_active(self) -> bool:
        return self.get_attribute(
            PasswordRecoveryPageLocators.NEW_PASSWORD, "type"
        ) == Texts.PASSWORD_TYPE_VISIBLE
    