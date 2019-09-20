from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Commons.basicPage import BasicPage
from PageLocators.login_page_element import login_page_element as ele


class loginPage(BasicPage):

    # 点击首页登陆按钮
    def click_login(self):
        handles = self.get_handles()
        self.click_element('首页', ele.index_login)
        return handles

    # 切换到账号密码登陆页面
    def login_page_swich(self, handles):
        self.swich_window(handles)

    # 登陆功能-输入用户名 密码点击登陆
    def login(self, username, pwd):
        self.input_text(model='用户登陆', locator=ele.username, content=username)
        self.input_text(model='用户登陆', locator=ele.password, content=pwd)
        self.click_element(model='用户登陆', locator=ele.login_button)

    # 获取错误提示-用户名密码错误
    def get_error_msg(self):
        error_msg = self.get_element_text(model='用户登陆', locator=ele.error_msg)
        return error_msg
