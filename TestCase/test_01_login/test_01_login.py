import unittest
import time
from selenium import webdriver
from PageObjects.login_page.Login_page import loginPage
from TestData.login_case_data import login_case_data as data


class testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.z-trip.cn")
        self.driver.maximize_window()

    def test_login_scuess(self):
        handle=loginPage(self.driver).click_login()
        loginPage(self.driver).swich_window(handle)
        loginPage(self.driver).login(username=data.username, pwd=data.pwd)
        time.sleep(2)

    def test_login_username_error(self):
        handle=loginPage(self.driver).click_login()
        loginPage(self.driver).swich_window(handle)
        loginPage(self.driver).login(username=data.error_username, pwd=data.pwd)
        errormsg = loginPage(self.driver).get_error_msg()
        self.assertEqual(data.error_msg, errormsg)
        time.sleep(1)

    def test_login_pwd_error(self):
        handle=loginPage(self.driver).click_login()
        loginPage(self.driver).swich_window(handle)
        loginPage(self.driver).login(username=data.username, pwd=data.error_pwd)
        errormsg = loginPage(self.driver).get_error_msg()
        self.assertEqual(data.error_msg, errormsg)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
