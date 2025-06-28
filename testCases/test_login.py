from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

import pytest

class TestLoginPage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_01_home_page_title(self, setup, test_logger):
        test_logger.info("******** Verifying home page title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        assert actual_title == expected_title, test_logger.error(f"expected title: {expected_title}, actual title: {actual_title}")


    def test_02_test_login(self, setup, test_logger):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.lp.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        assert actual_title == expected_title, test_logger.error(f"expected title: {expected_title}, actual title: {actual_title}")


