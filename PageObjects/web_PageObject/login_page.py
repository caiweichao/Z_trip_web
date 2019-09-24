from Commons.basicPage import BasicPage
from locator_and_datas.web_page_and_datas import login_page as login


class login_page(BasicPage):

    # 点击首页登陆按钮
    def click_login(self):
        handles = self.get_handles()
        self.click_element(login.welcome_page, login.index_login)
        return handles

    # 切换到账号密码登陆页面
    def login_page_swich(self, handles):
        self.swich_window(handles)

    # 登陆功能-输入用户名 密码点击登陆
    def login(self, username, pwd):
        self.input_text(model=login.describe, locator=login.username, content=username)
        self.input_text(model=login.describe, locator=login.password, content=pwd)
        self.click_element(model=login.describe, locator=login.login_button)

    # 获取错误提示-用户名密码错误
    def get_error_msg(self):
        error_msg = self.get_element_text(model=login.describe, locator=login.error_msg)
        return error_msg
