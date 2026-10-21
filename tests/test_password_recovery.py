import allure

from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from data.texts import Texts, RecoveryData


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_recovery_page(self, driver):
        login = LoginPage(driver)
        login.open()
        login.click_password_recovery()
        assert Texts.URL_PART_FORGOT_PASSWORD in login.get_current_url()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recovery_email_submit(self, driver):
        login = LoginPage(driver)
        login.open()
        login.click_password_recovery()

        recovery = PasswordRecoveryPage(driver)
        recovery.enter_email(RecoveryData.EMAIL)
        recovery.click_recovery()
        assert recovery.wait_reset_password_page()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_activates_field(self, driver):
        login = LoginPage(driver)
        login.open()
        login.click_password_recovery()

        recovery = PasswordRecoveryPage(driver)
        recovery.enter_email(RecoveryData.EMAIL)
        recovery.click_recovery()
        recovery.wait_reset_password_page()
        recovery.click_show_password()
        assert recovery.is_password_field_active()
        