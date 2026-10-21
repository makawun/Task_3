import allure

from pages.constructor_page import ConstructorPage 
from pages.personal_account_page import PersonalAccountPage
from data.texts import Texts


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_account(self, driver, authorized_user):
        page = ConstructorPage(driver)
        page.open()
        page.header.click_personal_account() 
        assert Texts.URL_PART_ACCOUNT_PROFILE in page.get_current_url()

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders_history(self, driver, authorized_user):
        page = ConstructorPage(driver)
        page.open()
        page.header.click_personal_account()

        account = PersonalAccountPage(driver)
        account.click_orders_history()
        assert Texts.URL_PART_ACCOUNT_ORDER_HISTORY in account.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_quit(self, driver, authorized_user):
        page = ConstructorPage(driver)
        page.open()
        page.header.click_personal_account()

        account = PersonalAccountPage(driver)
        account.click_quit()
        assert account.is_login_page()
        