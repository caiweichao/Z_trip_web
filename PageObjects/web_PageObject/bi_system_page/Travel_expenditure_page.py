from Commons.basicPage import BasicPage
from locator_and_datas.web_page_and_datas.bi_system_page import Travel_expenditure_page as data
from Commons import public_method


class travel_expenditure(BasicPage):
    # 点击出行类别标签
    def click_Travel_category(self):
        self.click_element(model=data.describe, locator=data.element_tab_Travel_category)

    # 点击下级单位标签
    def click_subordinate_unit(self):
        self.click_element(model=data.describe, locator=data.element_subordinate_unit)

    # 点击订单类型标签
    def click_order_type(self):
        self.click_element(model=data.describe,locator=data.element_order_type)

    # 点击查询按钮
    def click_quert(self):
        self.click_element(model=data.describe, locator=data.element_Query_button)

    def click_tab_order(self):
        self.click_element(model=data.describe, locator=data.element_tab_order)

    # 获取订单类型国际机票的标签
    def get_conntent_flight(self):
        return self.get_element_text(model=data.describe, locator=data.element_content_filght)

    # 获取出行类别表格标题
    def get_Travel_category(self):
        return self.get_element_text(model=data.describe, locator=data.element_Travel_category)

    # 获取差旅总支出金额
    def get_Total_travel_expenses(self):
        return self.get_element_text(model=data.describe, locator=data.element_Total_travel_expenses)

    # 点击日历中的上个月
    def query_the_previous_month_data(self):
        # 如果当前月份大于一月就直接选中上个月
        if public_method.get_now_month() > 1:
            self.click_element(model=data.describe,locator=data.element_Month_selector)
            self.click_element(model=data.describe,locator=data.element_get_mouth(public_method.get_now_month() - 1))
        else:
            self.click_element(model=data.describe,locator=data.element_year_selector)
            self.click_element(model=data.describe,locator=data.element_get_year(public_method.get_now_year() - 1))
            self.click_element(model=data.describe, locator=data.element_Month_selector)
            self.click_element(model=data.describe, locator=data.element_get_mouth(12))




