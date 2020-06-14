from selenium.webdriver.common.by import By



describe = '首页'
# -------------定位表达式---------------------
# 首页退出按钮
element_logout_icon =(By.XPATH,'//i[@class="iconfont icon-userback"]')
# 首页管理按钮
element_manage_icon =(By.XPATH,'//div[@data-popup="popup-manager"]')
# 首页设置按钮
element_set_icon = (By.XPATH,'//div[@data-popup="popup-setting"]')
# 管理菜单-差旅支出分析
element_Travel_expenditure = (By.XPATH,"//a[text()='- 差旅支出分析']")
# 管理菜单-差旅节支分析
element_Travel_savings_analysis = (By.XPATH,"//a[text()='- 差旅节支分析']")
# 管理菜单- 员工差标节支分析
element_Staff_standards = (By.XPATH,"//a[text()='- 员工差标节支分析']")
# 管理菜单- 员工违规分析
element_Employee_violation =(By.XPATH,"//a[text()='- 员工违规分析']")
# -------------测试数据------------------------

# -------------测试sql------------------------
