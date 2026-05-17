import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.login_page import Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

class TestDataDrivenLogin:

    page_url = Read_Config.get_page_url()
    # username = Read_Config.get_username()
    # password = Read_Config.get_password()
    # invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    path = ".//test_data//login_data.xlsx"

    status_list = []


    # def __init__(self,driver):
    #     self.driver = driver


    @pytest.mark.regression
    def test_valid_login_data_driven(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.page_url)

        self.login_page = Login_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("num of rows", self.rows)

        for r in range(2,self.rows+1):
             self.username = excel_utils.read_data(self.path, "Sheet1", r,1)
             self.password = excel_utils.read_data(self.path,"Sheet1", r,2)
             self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
             self.login_page.enter_username(self.username)
             self.login_page.enter_password(self.password)
             self.login_page.click_login()
             time.sleep(5)
             act_title = self.driver.find_element(By.CLASS_NAME,"title").text
             exp_title = "Products"

             if act_title == exp_title :
                 if self.exp_login == "yes":
                     self.logger.info("test data is passed")
                     self.status_list.append("Pass")
                     self.login_page.click_logout()
                 elif self.exp_login == "no":
                     self.logger.info("test data is failed")
                     self.status_list.append("Fail")

             elif   act_title!= exp_title :
                 if self.exp_login == "no":
                     self.logger.info("test data is passed")
                     self.status_list.append("Pass")
                 elif self.exp_login == "yes":
                     self.logger.info("test data is failed")
                     self.status_list.append("Fail")

        print("Status list is", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test  data driven test is failed")
            assert False
        else:
            self.logger.info("Test data driven test is passed")
            assert True
    @pytest.mark.sanity
    def test_invalid_login_data_driven(self, setup):

        self.driver = setup
        self.driver.get(self.page_url)

        self.login_page = Login_Page(self.driver)
        self.status_list = []

        self.rows = excel_utils.get_row_count(self.path, "Sheet2")

        for r in range(2, self.rows + 1):

            username = excel_utils.read_data(self.path, "Sheet2", r, 1)
            password = excel_utils.read_data(self.path, "Sheet2", r, 2)
            exp_login = excel_utils.read_data(self.path, "Sheet2", r, 3)

            self.login_page.enter_username(username)
            self.login_page.enter_password(password)
            self.login_page.click_login()

            try:
                act_error = self.driver.find_element(
                    By.XPATH, "//h3[@data-test='error']"
                ).text
            except:
                act_error = ""

            # If login successful, URL changes to inventory
            if "inventory" in self.driver.current_url:
                act_login = "yes"
                self.login_page.click_logout()
            else:
                act_login = "no"

            if act_login == exp_login:
                self.logger.info("Test Data Passed")
                self.status_list.append("Pass")
            else:
                self.logger.info("Test Data Failed")
                self.status_list.append("Fail")

            # Refresh for next iteration
            self.driver.get(self.page_url)

        if "Fail" in self.status_list:
            assert False
        else:
            assert True






