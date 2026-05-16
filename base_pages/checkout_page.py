from selenium.webdriver.common.by import By


class Checkout_Page:

    # Step 1: Checkout Information page
    first_name_id = "first-name"
    last_name_id = "last-name"
    postal_code_id = "postal-code"
    continue_btn_id = "continue"

    # Step 2 (optional verification)
    checkout_title_xpath = "//span[@class='title']"

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.ID, self.postal_code_id).clear()
        self.driver.find_element(By.ID, self.postal_code_id).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID, self.continue_btn_id).click()

    def get_checkout_title(self):
        return self.driver.find_element(By.XPATH, self.checkout_title_xpath).text