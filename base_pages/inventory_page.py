from selenium.webdriver.common.by import By

class InventoryPage:

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()