from PageObjects.web_PageObject.login_page import login_page
from locator_and_datas.web_page_and_datas import login_page as data
from PageObjects.web_PageObject.index_page import indexPage
from locator_and_datas.web_page_and_datas import index_page as indexdata
from Commons.Config import ConfigLoader
import pytest
import allure


@pytest.mark.usefixtures("open_windows")
@allure.feature('登录测试用例集合')
@allure.issue('http://192.168.1.201:18900/browse/PLATFORM-516')
class Test_login():
    @allure.story('登录成功')
    def test_login_success(self, open_windows):
        handle = login_page(open_windows).click_login()
        #正式环境才会切换句柄
        if ConfigLoader().get_basic_conf() == 'PRO':
            login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.pwd)
        assert indexPage(open_windows).get_element_text(indexdata.describe, indexdata.element_set_icon) == '设置'

    @allure.story('登录失败-用户名错误')
    def test_login_username_error(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.errorUsername, data.pwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg

    @allure.story('登录失败-密码错误')
    def test_login_password_error(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.errorPwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg

    @allure.story('登录成功后退出登录')
    def test_logout(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.pwd)
        indexPage(open_windows).click_logout_icon()
        assert login_page(open_windows).get_element_text(data.describe, data.element_index_login) == '立即登录'
