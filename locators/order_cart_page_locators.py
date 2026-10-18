from selenium.webdriver.common.by import By

class OrderCartPageLocators:
    
    ORDER_NUMBER = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

    CLOSE_BUTTON = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    