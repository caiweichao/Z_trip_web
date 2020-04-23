from Commons.basicPage import BasicPage
from locator.web_page import index_page as index
import allure


class indexPage(BasicPage):
    @allure.step("点击首页设置按钮")
    def click_index_set_icon(self):
        self.click_element(index.describe, index.element_set_icon)

    @allure.step("点击首页管理按钮")
    def click_index_manage_icon(self):
        self.click_element(index.describe, index.element_manage_icon)

    @allure.step("点击管理菜单-差旅支出分析")
    def click_Travel_expenditure(self):
        self.click_element(index.describe, index.element_Travel_expenditure)

    @allure.step("点击管理菜单-差旅节支分析")
    def click_Travel_savings_analysis(self):
        self.click_element(index.describe, index.element_Travel_savings_analysis)

    @allure.step("点击管理菜单-员工差标节支分析")
    def click_Staff_standards(self):
        self.click_element(index.describe, index.element_Staff_standards)

    @allure.step("点击管理菜单-员工违规分析")
    def click_Employee_violation(self):
        self.click_element(index.describe, index.element_Employee_violation)

    @allure.step("点击首页退出按钮")
    def click_logout_icon(self):
        self.click_element(index.describe, index.element_logout_icon)
