import time

from pageObjects.LoginPage import LoginPage
from utilities import XLUtils

class TestDataDriven:
    baseURL = "https://admin-demo.nopcommerce.com/"
    path = "..//TestData/LoginData.xlsx"

    def test_01_login_data_driven(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        row_count = XLUtils.getRowCount(self.path, "Sheet1")
        column_count = XLUtils.getColumnCount(self.path, "Sheet1")

        lst_status = []
        for row in range(2, row_count + 1):
            self.username = XLUtils.readData(self.path, "Sheet1", row, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", row, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", row, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            actual_title = self.lp.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                if self.exp == "Pass":
                    print("passed")
                    self.lp.clickLogout()
                    time.sleep(60)
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    print("failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    print("failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    print("passed")
                    lst_status.append("Pass")

        assert "Fail" in lst_status, "data driven testing was unsuccessful"

