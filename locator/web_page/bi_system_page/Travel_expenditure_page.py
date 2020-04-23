from selenium.webdriver.common.by import By

# 页面描述
describe = "差旅支出分析"
# -------------定位表达式---------------------
# 差旅总支出金额
element_Total_travel_expenses = (By.XPATH, '//p[text()="差旅总支出"]//parent::div//span')
# 订单类型TAB-国内机票
element_content_filght = (By.XPATH, '//span[text()="国内机票"]')
# TAV-订单类型
element_order_type = (By.XPATH,'//div[@class="ivu-tabs-nav-scroll"]//*[text()=" 订单类型 "]')
# TAB-出行类别
element_tab_Travel_category = (By.XPATH, '//div[@class="ivu-tabs-nav-scroll"]//*[text()=" 出行类别 "]')
# TAB-订单类型
element_tab_order = (By.XPATH, '//div[@class="ivu-tabs-nav-scroll"]//*[text()=" 订单类型 "]')
# 出行类别表格标题
element_Travel_category = (By.XPATH, '//div[@class="ivu-table-cell"]//span[text()="出行类别"]')
# TAB-下级单位
element_subordinate_unit = (By.XPATH, '//*[text()=" 下级单位 "]')
# 月份选择器
element_Month_selector = (By.XPATH, '//div[@class="search-month ivu-date-picker"]//input')
# 年份选择器
element_year_selector = (By.XPATH,'//div[@class="ivu-date-picker"]')
# 查询按钮
element_Query_button = (By.XPATH, '//span[@class="search-btn"]')


# 需要被选中的月份
def element_get_mouth(data):
    element_now_mouth = (
    By.XPATH, '//div[@class="ivu-date-picker-cells ivu-date-picker-cells-month"]//em[text()="{}月"]'.format(data))
    return element_now_mouth


# 需要被选中的年份
def element_get_year(data):
    element_now_year = (
    By.XPATH, '//div[@class="ivu-date-picker-cells ivu-date-picker-cells-year"]//em[text()="{}"]'.format(data))
    return element_now_year
# -------------测试数据------------------------

# -------------测试sql------------------------
