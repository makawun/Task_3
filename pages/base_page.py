import time

import allure
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from data.urls import Urls
from data.texts import Timeouts


class BasePage:
    def __init__(self, driver):
            self.__driver = driver
            self.wait = WebDriverWait(driver, Timeouts.DEFAULT)
            self.header = HeaderComponent(self)

    @allure.step("Открыть страницу: {path}")
    def open(self, path: str = Urls.MAIN):
        self.__driver.get(f"{Urls.BASE_URL}{path}")

    def get_current_url(self) -> str:
        return self.__driver.current_url

    def get_page_source(self) -> str:
        return self.__driver.page_source

    def wait_url_contains(self, fragment: str, timeout: int = Timeouts.LONG) -> bool:
        return self.wait.until(
            EC.url_contains(fragment),
            message=f"URL не содержит '{fragment}' за {timeout} c",
        )

    def wait_url_equals(self, url: str, timeout: int = Timeouts.LONG) -> bool:
        expected = url.rstrip("/")
        return self.wait.until(
            lambda d: d.current_url.rstrip("/") == expected,
            message=f"URL не стал '{expected}' за {timeout} c",
        )

    def wait_url_not_contains(self, fragment: str, timeout: int = Timeouts.LONG) -> bool:
        return self.wait.until(
            lambda d: fragment not in d.current_url,
            message=f"URL всё ещё содержит '{fragment}' за {timeout} c",
        )

    def wait_overlay_gone(self, timeout: int = 3):
        self.wait.until(
            EC.invisibility_of_element_located(BasePageLocators.MODAL_OVERLAY),
            message="Оверлей модального окна не исчез",
        )

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator) -> list:
        return self.__driver.find_elements(*locator)

    def find_all_visible(self, locator) -> list:
        return [el for el in self.find_all(locator) if el.is_displayed()]

    def click(self, locator):
        try:
            self.wait_overlay_gone()
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except (TimeoutException, ElementClickInterceptedException):
            self.js_click(locator)

    def send_keys(self, locator, value: str):
        self.find_visible(locator).send_keys(value)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)
        self.__driver.execute_script(
            "function ev(t){return new DragEvent(t,{bubbles:true});}"
            "arguments[0].dispatchEvent(ev('dragstart'));"
            "arguments[1].dispatchEvent(ev('drop'));",
            source, target,
        )

    def js_click(self, locator):
        element = self.find(locator)
        self.__driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def get_attribute(self, locator, name: str):
        return self.find_visible(locator).get_attribute(name)

    def wait_until_text_contains(self, locator, expected: str, timeout: int = Timeouts.LONG) -> bool:
        end = time.time() + timeout
        while time.time() < end:
            try:
                if expected in self.get_text(locator):
                    return True
            except Exception:
                pass
            time.sleep(Timeouts.POLL_INTERVAL)
        return False

    def wait_until_counter_grows(self, locator, before: int, timeout: int = Timeouts.LONG) -> bool:
        end = time.time() + timeout
        while time.time() < end:
            try:
                if int(self.get_text(locator)) > before:
                    return True
            except Exception:
                pass
            time.sleep(Timeouts.POLL_INTERVAL)
        return False

class HeaderComponent:
    def __init__(self, page):
        self._page = page

    @allure.step("Клик по «Личный кабинет»")
    def click_personal_account(self):
        self._page.click(BasePageLocators.PERSONAL_ACCOUNT)
        self._page.wait_url_contains(Urls.ACCOUNT_PROFILE)

    @allure.step("Клик по «Лента заказов»")
    def click_order_tape(self):
        self._page.click(BasePageLocators.ORDER_TAPE)
        self._page.wait_url_contains(Urls.FEED)

    @allure.step("Клик по «Конструктор»")
    def click_constructor(self):
        self._page.click(BasePageLocators.CONSTRUCTOR)
        self._page.wait_url_equals(Urls.BASE_URL)
        