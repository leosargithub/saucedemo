import time

import  pytest
from  selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.login_page import Login_Page

from utilities.read_properties import Read_Config
from  utilities.custom_logger import Log_Maker



class Test_01_Login:
    page_url = Read_Config.get_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()
    logger = Log_Maker.log_gen()

    def test_valid_login(self,setup):
        self.logger.info("*************Test_Valid_login***********")
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()

        act_logo_text = self.driver.find_element(By.CLASS_NAME,"app_logo").text
        if act_logo_text == "Swag Labs":
            self.logger.info("*************Logo_test_matched***********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
            assert False



    def test_invalid_login(self,setup):
        self.logger.info("*************Test_invalid_login***********")
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_page = Login_Page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.invalid_password)
        self.login_page.click_login()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text

        if error_message == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("*************Username and password not matched ***********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.driver.close()
            assert False


