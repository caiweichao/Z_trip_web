from selenium.webdriver.common.by import By

# 页面描述
welcome_page = '欢迎'
describe = "登录"
# -------------定位表达式---------------------
# 正式环境首页立即登陆按钮
element_index_login = (By.XPATH, '//a[@id="btn-login"]')
# sit、uat环境首页立即登陆按钮
element_test_index_login = (By.XPATH, '//a[@class="login"]')
# 用户登陆页面用户名
element_username = (By.XPATH, '//input[@name="username"]')
# 用户登陆页面密码
element_password = (By.XPATH, '//input[@id="submitLogin"]')
# 用户登陆页面-立即登陆按钮
element_login_button = (By.XPATH, '//input[@class="input_login login_btn"]')
# uat——test环境
element_login_button_uat_test =(By.XPATH,'//a[@class="login"]')
# 错误信息提示
element_error_msg = (By.XPATH, '//div[@id="msg-box"]')

# -------------测试数据------------------------
userName = 13248231369
errorUsername = 132482313691
pwd = 'cai123456'
errorPwd = 111111
errorMsg = '用户名密码错误'
# -------------测试sql------------------------
