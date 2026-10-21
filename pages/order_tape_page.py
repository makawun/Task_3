import time

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_tape_page_locators import OrderTapePageLocators
from data.urls import Urls
from data.texts import Timeouts


class OrderTapePage(BasePage):
    @staticmethod
    def _normalize(text: str) -> str:
        return text.replace("#", "").strip().lstrip("0")

    @allure.step("Открыть ленту заказов")
    def open(self):
        super().open(Urls.FEED)
        self.wait_url_contains(Urls.FEED)

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.click(OrderTapePageLocators.ORDER_CART)

    @allure.step("Клик по заказу с номером {order_number}")
    def click_order_by_number(self, order_number: str):
        normalized = self._normalize(order_number)
        locator = (
            By.XPATH,
            f".//ul[contains(@class, 'OrderFeed_list')]"
            f"//p[contains(@class, 'text_type_digits-default') "
            f"and contains(translate(text(), '#', ''), '{normalized}')]/ancestor::a"
        )
        self.click(locator)

    @allure.step("Проверить, что модалка заказа {order_number} открыта")
    def is_order_modal_open(self, order_number: str) -> bool:
        self.find_visible(OrderTapePageLocators.ORDER_MODAL_NUMBER)
        text = self.get_text(OrderTapePageLocators.ORDER_MODAL_NUMBER)
        return self._normalize(text) == self._normalize(order_number)

    @allure.step("Получить номер первого заказа в списке")
    def get_first_order_number(self) -> str:
        return self.get_text(OrderTapePageLocators.FIRST_ORDER_NUMBER)

    @allure.step("Дождаться появления заказа {order_number} в списке заказов")
    def wait_order_number_in_list(self, order_number: str, timeout: int = Timeouts.LONG) -> bool:
        expected = self._normalize(order_number)
        end = time.time() + timeout
        while time.time() < end:
            try:
                if self._normalize(self.get_first_order_number()) == expected:
                    return True
            except Exception:
                pass
            time.sleep(Timeouts.POLL_INTERVAL)
        return False

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_all_orders_counter(self) -> int:
        return int(self.get_text(OrderTapePageLocators.ALL_ORDERS_COUNTER))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders_counter(self) -> int:
        return int(self.get_text(OrderTapePageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Дождаться, пока счётчик «всего» вырастет с {before}")
    def wait_all_counter_grows(self, before: int) -> bool:
        return self.wait_until_counter_grows(OrderTapePageLocators.ALL_ORDERS_COUNTER, before)

    @allure.step("Дождаться, пока счётчик «сегодня» вырастет с {before}")
    def wait_today_counter_grows(self, before: int) -> bool:
        return self.wait_until_counter_grows(OrderTapePageLocators.TODAY_ORDERS_COUNTER, before)

    @allure.step("Дождаться появления заказа {order_number} в «В работе»")
    def wait_order_in_process(self, order_number: str) -> bool:
        return self.wait_until_text_contains(
            OrderTapePageLocators.IN_PROCESS_ORDERS_LAST_ELEMENT, order_number
        )
    