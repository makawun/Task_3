import time

import allure

from pages.base_page import BasePage
from locators.order_cart_page_locators import OrderCartPageLocators
from data.texts import Texts, Timeouts


class OrderCartPage(BasePage):
    @allure.step("Дождаться реального номера заказа (игнорируя заглушку 9999)")
    def wait_real_order_number(self, timeout: int = Timeouts.LONG) -> str:
        #для скипа заглушки
        end = time.time() + timeout
        while time.time() < end:
            try:
                value = self.get_text(OrderCartPageLocators.ORDER_NUMBER).strip()
                if value and value != Texts.ORDER_NUMBER_PLACEHOLDER:
                    return value
            except Exception:
                pass
            time.sleep(Timeouts.POLL_INTERVAL)
        raise AssertionError(
            f"Реальный номер заказа не появился за {timeout} c "
            f"(заглушка '{Texts.ORDER_NUMBER_PLACEHOLDER}' так и осталась)"
        )

    @allure.step("Закрыть модалку заказа")
    def close(self):
        self.click(OrderCartPageLocators.CLOSE_BUTTON)
        