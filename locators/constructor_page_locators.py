from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    CR_BUN = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a32b']")
    CR_BUN_COUNTER = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a32b']/div/p[@class='counter_counter__num__3nue1']")

    SPACE_SAUCE = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a332']")
    SPACE_SAUCE_COUNTER = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a332']/div/p[@class='counter_counter__num__3nue1']")

    MEAT = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a32e']")
    MEAT_COUNTER = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']/a[@href='/ingredient/6acef97852135b001b21a32e']/div/p[@class='counter_counter__num__3nue1']")

    ORDER_LOCATION = (By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']/span[@class='constructor-element__row']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    