import unittest
import time
from selenium import webdriver
from PageObjects.Index_page import indexpage
from PageObjects.Login_page import loginPage
from PageObjects.Home_page import homePage


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.z-trip.cn")
        self.driver.maximize_window()

    def test_login_scuess(self):
        # 进入首页
        indexpage(self.driver).click()
        # 输入用户名密码点击登陆
        loginPage(self.driver).login(username='13248231369', pwd='1995030226')
        self.assertTrue(homePage(self.driver).isexit())

    # 登陆失败
    def test_login_fail(self):
        indexpage(self.driver).click()
        loginPage(self.driver).login(username='13248231369', pwd='123123')
        self.assertEqual(loginPage(self.driver).error_msg(), '用户名密码错误')

    def tearDown(self):
        self.driver.quit()
