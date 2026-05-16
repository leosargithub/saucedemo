import pytest

from base_pages.login_page import Login_Page
from base_pages.inventory_page import InventoryPage
from base_pages.cart_page import CartPage
from base_pages.checkout_page import Checkout_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_Checkout:

    page_url = Read_Config.get_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    logger = Log_Maker.log_gen()

    def test_checkout_flow(self, setup):

        self.logger.info("************* Checkout Test Started *************")

        self.driver = setup
        self.driver.get(self.page_url)

        # Login
        login = Login_Page(self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        # Inventory
        inventory = InventoryPage(self.driver)
        inventory.add_item_to_cart()
        inventory.open_cart()

        # Cart
        cart = CartPage(self.driver)
        cart.click_checkout()

        # Checkout Step 1
        checkout = Checkout_Page(self.driver)
        checkout.enter_first_name("John")
        checkout.enter_last_name("Doe")
        checkout.enter_postal_code("12345")
        checkout.click_continue()



        self.logger.info("************* Checkout Test Passed *************")