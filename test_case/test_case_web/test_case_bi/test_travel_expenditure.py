import allure
import pytest

from PageObjects.web_PageObject.bi_system_page.Travel_expenditure_page import travel_expenditure
from PageObjects.web_PageObject.index_page import indexPage


@pytest.mark.usefixtures("login_all_case")
@allure.feature('差旅支出统计页面用例集合')
class Test_travel_expenditure():
    @allure.step('进入差旅支出统计页面')
    def test_into_travel_expenditure_page(self, login_all_case):
        indexPage(login_all_case).click_index_manage_icon()
        indexPage(login_all_case).click_Travel_expenditure()
        travel_expenditure(login_all_case).get_conntent_flight()
        with allure.step('开始进行校验差旅总支出金额'):
            assert travel_expenditure(login_all_case).get_Total_travel_expenses() == '9504.5'
        travel_expenditure(login_all_case).allure_img()

    @allure.step('点击出行类别tab')
    def test_click_tab_Travel_category(self, login_all_case):
        travel_expenditure(login_all_case).click_Travel_category()
        with allure.step('开始进行校验出行类别表单金额'):
            assert travel_expenditure(login_all_case).get_Travel_category() == '出行类别'
        travel_expenditure(login_all_case).allure_img()

    @allure.step('点击下级单位tab')
    def test_click_tab_subordinate_unit(self, login_all_case):
        travel_expenditure(login_all_case).click_subordinate_unit()
        travel_expenditure(login_all_case).allure_img()

    @allure.step('点击订单类型')
    def test_click_tab_OrderType(self, login_all_case):
        travel_expenditure(login_all_case).click_order_type()
        travel_expenditure(login_all_case).allure_img()

    @allure.step('查询上个月的数据')
    def test_Query_the_previous_month_data(self, login_all_case):
        import time
        time.sleep(1)
        travel_expenditure(login_all_case).click_order_type()
        travel_expenditure(login_all_case).query_the_previous_month_data()
        travel_expenditure(login_all_case).click_quert()
        travel_expenditure(login_all_case).get_conntent_flight()
        time.sleep(1)
        with allure.step('开始进行校验差旅总支出金额'):
            assert travel_expenditure(login_all_case).get_Total_travel_expenses() == '0'
        travel_expenditure(login_all_case).allure_img()

