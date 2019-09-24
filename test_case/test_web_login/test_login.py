from PageObjects.login.Login_page import login_page
from locator_and_datas import login_page_element_and_data as data
import pytest


@pytest.mark.usefixtures("open_windows")
class Test_login():
    def test_login_success(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.pwd)


    def test_login_username_error(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.errorUsername, data.pwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg

    def test_login_password_error(self, open_windows):
        handle = login_page(open_windows).click_login()
        login_page(open_windows).login_page_swich(handle)
        login_page(open_windows).login(data.userName, data.errorPwd)
        assert login_page(open_windows).get_error_msg() == data.errorMsg
