from selenium.webdriver.common.by import By

class CartPage:

    checkout_btn_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, self.checkout_btn_id).click()