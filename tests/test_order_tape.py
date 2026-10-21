import allure

from pages.constructor_page import ConstructorPage
from pages.order_cart_page import OrderCartPage
from pages.order_tape_page import OrderTapePage


@allure.feature("Лента заказов")
class TestOrderTape:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver, authorized_user):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.add_bun()
        constructor.click_create_order()

        cart = OrderCartPage(driver)
        order_number = cart.wait_real_order_number()
        cart.close()

        tape = OrderTapePage(driver)
        tape.open()
        tape.click_order_by_number(order_number)
        assert tape.is_order_modal_open(order_number)

    @allure.title("Заказы пользователя из «Истории заказов» отображаются в «Ленте заказов»")
    def test_user_order_visible_in_tape(self, driver, authorized_user):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.add_bun()
        constructor.click_create_order()

        cart = OrderCartPage(driver)
        order_number = cart.wait_real_order_number()
        cart.close()

        tape = OrderTapePage(driver)
        tape.open()
        assert tape.wait_order_number_in_list(order_number)

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_all_orders_counter_increases(self, driver, authorized_user):
        tape = OrderTapePage(driver)
        tape.open()
        before = tape.get_all_orders_counter()

        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.add_bun()
        constructor.click_create_order()

        cart = OrderCartPage(driver)
        cart.wait_real_order_number()
        cart.close()

        tape.open()
        assert tape.wait_all_counter_grows(before)
        assert tape.get_all_orders_counter() > before

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, driver, authorized_user):
        tape = OrderTapePage(driver)
        tape.open()
        before = tape.get_today_orders_counter()

        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.add_bun()
        constructor.click_create_order()

        cart = OrderCartPage(driver)
        cart.wait_real_order_number()
        cart.close()

        tape.open()
        assert tape.wait_today_counter_grows(before)
        assert tape.get_today_orders_counter() > before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_in_process(self, driver, authorized_user):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.add_bun()
        constructor.click_create_order()

        cart = OrderCartPage(driver)
        order_number = cart.wait_real_order_number()
        cart.close()

        tape = OrderTapePage(driver)
        tape.open()
        assert tape.wait_order_in_process(order_number)
        