import time

import allure

from pages.base_page import BasePage
from locators.ingredients_details_page_locators import IngredientsDetailsPageLocators


class IngredientsDetailsPage(BasePage):
    @allure.step("Закрыть модалку крестиком")
    def close(self):
        self.js_click(IngredientsDetailsPageLocators.CLOSE_BUTTON)

    @allure.step("Проверить, что модалка открыта")
    def is_open(self) -> bool:
        return self.find_visible(IngredientsDetailsPageLocators.CART_NAME).is_displayed()

    @allure.step("Дождаться, что модалка закрыта")
    def wait_closed(self, timeout: int = 5) -> bool:
        end = time.time() + timeout
        while time.time() < end:
            if len(self.find_all_visible(IngredientsDetailsPageLocators.CART_NAME)) == 0:
                return True
            time.sleep(0.3)
        return False

    @allure.step("Проверить, что модалка скрыта")
    def is_closed(self) -> bool:
        return len(self.find_all_visible(IngredientsDetailsPageLocators.CART_NAME)) == 0
    