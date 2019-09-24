from Commons.basicPage import BasicPage
from locator_and_datas.web_page_and_datas import index_page as index


class indexPage(BasicPage):
    # 点击首页设置按钮
    def click_index_set_icon(self):
        self.click_element(index.describe, index.element_set_icon)

    # 点击首页管理按钮
    def click_index_manage_icon(self):
        self.click_element(index.describe, index.element_manage_icon)

    # 点击管理菜单-差旅支出分析
    def click_Travel_expenditure(self):
        self.click_element(index.describe,index.element_Travel_expenditure)

    # 点击管理菜单-差旅节支分析
    def click_Travel_savings_analysis(self):
        self.click_element(index.describe,index.element_Travel_savings_analysis)

    # 点击管理菜单-员工差标节支分析
    def click_Staff_standards(self):
        self.click_element(index.describe,index.element_Staff_standards)

    # 点击管理菜单-员工违规分析


    # 点击首页退出按钮
    def click_logout_icon(self):
        self.click_element(index.describe,index.element_logout_icon)

    # 获取退出按钮
    def get_logout_icon(self):
        element = self.find_element(index.describe,index.element_logout_icon)
        return element