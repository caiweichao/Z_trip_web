import pytest
from selenium import webdriver
from Commons import Contans
from Commons.MysqlConnect import Mysql_Util
from Commons.Config import ConfigLoader
from PageObjects.web_PageObject.login_page import login_page
from locator_and_datas.web_page_and_datas import login_page as data


@pytest.fixture()
# 打开浏览器 --每条用例执行都会调用一次
def open_windows():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=Contans.url)
    yield driver
    login_page(driver).allure_img()
    # 一个用例执行完毕后执行yield后的代码
    driver.close()


@pytest.fixture()
# 完成用户登录
def login():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=Contans.url)
    handle = login_page(driver).click_login()
    if ConfigLoader().get_basic_conf() == 'PRO':
        login_page(driver).login_page_swich(handle)
    login_page(driver).login(data.userName, data.pwd)
    yield driver
    # 一个用例执行完毕后执行yield后的代码
    driver.quit()

@pytest.fixture(scope='session')
# 完成用户登录,全部case执行完毕再次关闭浏览器
def login_one():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=Contans.url)
    handle = login_page(driver).click_login()
    if ConfigLoader().get_basic_conf() == 'PRO':
        login_page(driver).login_page_swich(handle)
    login_page(driver).login(data.userName, data.pwd)
    yield driver
    # 一个用例执行完毕后执行yield后的代码
    driver.quit()

# 链接数据库使用session参数 一个测试用例集合之前执行 不是每一条用例之前执行减少重复调用提升性能
@pytest.fixture(scope='session')
def mysql_connect():
    #实例化数据库链接
    connect = Mysql_Util()
    #一个测试类执行完毕之后关闭数据库链接
    yield connect
    connect.close_connect()


