import pytest
import allure
from PageObjects.web_PageObject.index_page import indexPage
from PageObjects.web_PageObject.bi_system_page.Travel_expenditure_page import travel_expenditure

@pytest.mark.usefixtures("login_one")
@allure.feature('差旅支出统计页面用例集合')
class Test_travel_expenditure():
    @allure.story('进入差旅支出统计页面')
    def test_into_travel_expenditure_page(self,login_one):
        indexPage(login_one).click_index_manage_icon()
        indexPage(login_one).click_Travel_expenditure()
        travel_expenditure(login_one).get_conntent_flight()
        with allure.step('开始进行校验差旅总支出金额'):
            assert travel_expenditure(login_one).get_Total_travel_expenses() == '0'
        travel_expenditure(login_one).allure_img()

    @allure.story('点击出行类别tab')
    def test_click_tab_Travel_category(self,login_one):
        travel_expenditure(login_one).click_Travel_category()
        with allure.step('开始进行校验出行类别表单金额'):
            assert travel_expenditure(login_one).get_Travel_category() =='出行类别'
        travel_expenditure(login_one).allure_img()

    @allure.story('点击下级单位tab')
    def test_click_tab_subordinate_unit(self,login_one):
        travel_expenditure(login_one).click_subordinate_unit()
        with allure.step('开始进行下级单位tab校验'):
            assert travel_expenditure(login_one).get_Travel_category() == '出行类别'
        travel_expenditure(login_one).allure_img()

    @allure.story('查询上个月的数据')
    def test_Query_the_previous_month_data(self,login_one):
        import time
        time.sleep(1)
        travel_expenditure(login_one).click_order_type()
        travel_expenditure(login_one).query_the_previous_month_data()
        travel_expenditure(login_one).click_quert()
        travel_expenditure(login_one).get_conntent_flight()
        with allure.step('开始进行校验差旅总支出金额'):
            assert travel_expenditure(login_one).get_Total_travel_expenses() == '0'
        travel_expenditure(login_one).allure_img()



