from selenium.webdriver.common.by import By


class Login_Page:
    username_id = "user-name"
    password_id = "password"
    btn_login_id = "login-button"
    hamburger_id = "react-burger-menu-btn"
    btn_logout_id = "logout_sidebar_link"


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def  click_login(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()

    def  click_logout(self):
        self.driver.find_element(By.ID, self.hamburger_id).click()
        self.driver.find_element(By.ID,self.btn_logout_id).click()












