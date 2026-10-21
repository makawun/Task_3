from selenium.webdriver.common.by import By


class OrderTapePageLocators:
    ORDER_CART = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a")

    FIRST_ORDER_NUMBER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class, 'text_type_digits-default')]")

    ORDER_MODAL_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[contains(@class, 'text_type_digits-default')]")

    ALL_ORDERS_COUNTER = (By.XPATH, ".//div[@class='undefined mb-15']//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    TODAY_ORDERS_COUNTER = (By.XPATH, ".//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    IN_PROCESS_ORDERS_LAST_ELEMENT = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[1]")
    