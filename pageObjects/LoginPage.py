from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = ".//button[@class='button-1 login-button'][text()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        elem = self.driver.find_element(By.ID, self.textbox_username_id)
        elem.clear()
        elem.send_keys(username)
        return

    def setPassword(self, password):
        elem = self.driver.find_element(By.ID, self.textbox_password_id)
        elem.clear()
        elem.send_keys(password)
        return

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))
        elem.click()
        