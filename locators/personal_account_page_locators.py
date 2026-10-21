from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    
    ORDERS_HISTORY = (By.XPATH, ".//a[text()='История заказов']")

    QUIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    