import allure

from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from data.urls import Urls


class ConstructorPage(BasePage):
    @allure.step("Открыть конструктор")
    def open(self):
        super().open(Urls.MAIN)
        self.wait_url_equals(Urls.BASE_URL)

    @allure.step("Клик по булочке")
    def click_bun(self):
        self.click(ConstructorPageLocators.CR_BUN)

    @allure.step("Получить счётчик булочки")
    def get_bun_counter(self) -> int:
        text = self.get_text(ConstructorPageLocators.CR_BUN_COUNTER)
        return int(text) if text else 0

    @allure.step("Добавить булочку в заказ")
    def add_bun(self):
        self.drag_and_drop(
            ConstructorPageLocators.CR_BUN,
            ConstructorPageLocators.ORDER_LOCATION,
        )

    @allure.step("Получить счётчик соуса")
    def get_sauce_counter(self) -> int:
        text = self.get_text(ConstructorPageLocators.SPACE_SAUCE_COUNTER)
        return int(text) if text else 0

    @allure.step("Добавить соус в заказ")
    def add_sauce(self):
        self.drag_and_drop(
            ConstructorPageLocators.SPACE_SAUCE,
            ConstructorPageLocators.ORDER_LOCATION,
        )

    @allure.step("Получить счётчик мяса")
    def get_meat_counter(self) -> int:
        text = self.get_text(ConstructorPageLocators.MEAT_COUNTER)
        return int(text) if text else 0

    @allure.step("Добавить мясо в заказ")
    def add_meat(self):
        self.drag_and_drop(
            ConstructorPageLocators.MEAT,
            ConstructorPageLocators.ORDER_LOCATION,
        )

    @allure.step("Клик по «Оформить заказ»")
    def click_create_order(self):
        self.click(ConstructorPageLocators.CREATE_ORDER_BUTTON)
