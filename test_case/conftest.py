import pytest
from selenium import webdriver
from Commons import Contans
from PageObjects.login.Login_page import login_page
from locator_and_datas.login_page_locator_and_data import login_page_element_and_data as data

@pytest.fixture()
# 打开浏览器
def open_windows():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=Contans.url)
    yield driver
    driver.quit()

@pytest.fixture()
# 完成用户登录
def login():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=Contans.url)
    handle = login_page(driver).click_login()
    login_page(driver).login_page_swich(handle)
    login_page(driver).login(data.userName,data.pwd)
    yield driver




