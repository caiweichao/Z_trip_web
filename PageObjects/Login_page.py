from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    # 登陆功能
    def login(self, username, pwd):
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
        self.driver.find_element_by_xpath('//input[@class="input_login login_btn"]').click()

    # 获取错误提示-用户名密码错误
    def error_msg(self):
        WebDriverWait(self.driver, 20). \
            until(EC.visibility_of_element_located((By.XPATH, '//div[text()="用户名密码错误"]')))
        element = self.driver.find_element_by_xpath('//div[text()="用户名密码错误"]').text
        return element
