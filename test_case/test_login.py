from selenium import webdriver
from PageObjects.login.Login_page import login_page
from locator_and_datas.login_page_locator_and_data import login_page_element_and_data as data
import pytest
import time


@pytest.mark.usefixtures("open_windows")
class test_login():
    def test_login_success(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.pwd)
        time.sleep(1)

    def test_login_username_errpr(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.errorUsername, data.pwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg
        time.sleep(1)

    def test_login_password_errpr(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.errorPwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(['-q', 'test_login.py'])