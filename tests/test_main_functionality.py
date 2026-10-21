import allure

from pages.constructor_page import ConstructorPage
from pages.ingredients_details_page import IngredientsDetailsPage
from pages.order_cart_page import OrderCartPage
from pages.personal_account_page import PersonalAccountPage
from data.urls import Urls
from data.texts import Texts, IngredientDelta


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        page = ConstructorPage(driver)
        page.open()
        page.header.click_order_tape()
        page.header.click_constructor()
        assert page.get_current_url().rstrip("/") == Urls.BASE_URL

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_tape(self, driver):
        page = ConstructorPage(driver)
        page.open()
        page.header.click_order_tape()
        assert Texts.URL_PART_FEED in page.get_current_url()

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, driver):
        page = ConstructorPage(driver)
        page.open()
        page.click_bun()

        details = IngredientsDetailsPage(driver)
        assert details.is_open()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        page = ConstructorPage(driver)
        page.open()
        page.click_bun()

        details = IngredientsDetailsPage(driver)
        details.close()
        details.wait_closed()
        assert details.is_closed()

    @allure.title("Добавление булочки увеличивает её счётчик на 2")
    def test_bun_counter_increases_by_two(self, driver):
        page = ConstructorPage(driver)
        page.open()
        before = page.get_bun_counter()
        page.add_bun()
        after = page.get_bun_counter()
        assert after == before + IngredientDelta.BUN

    @allure.title("Добавление соуса увеличивает его счётчик на 1")
    def test_sauce_counter_increases_by_one(self, driver):
        page = ConstructorPage(driver)
        page.open()
        before = page.get_sauce_counter()
        page.add_sauce()
        after = page.get_sauce_counter()
        assert after == before + IngredientDelta.SAUCE

    @allure.title("Добавление мяса увеличивает его счётчик на 1")
    def test_meat_counter_increases_by_one(self, driver):
        page = ConstructorPage(driver)
        page.open()
        before = page.get_meat_counter()
        page.add_meat()
        after = page.get_meat_counter()
        assert after == before + IngredientDelta.MEAT

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, authorized_user):
        page = ConstructorPage(driver)
        page.open()
        page.add_bun()
        page.click_create_order()

        cart = OrderCartPage(driver)
        order_number = cart.wait_real_order_number()
        cart.close()

        page.header.click_personal_account()
        account = PersonalAccountPage(driver)
        account.click_orders_history()
        assert order_number in account.get_page_source()
        