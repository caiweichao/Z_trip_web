from selenium.webdriver.common.by import By

# 页面描述
welcome_page = '欢迎页'
describe = "登录页面"
# -------------定位表达式---------------------
# 首页立即登陆按钮
index_login = (By.XPATH, '//a[@id="btn-login"]')
# 用户登陆页面用户名
username = (By.XPATH, '//input[@name="username"]')
# 用户登陆页面密码
password = (By.XPATH, '//input[@id="submitLogin"]')
# 用户登陆页面-立即登陆按钮
login_button = (By.XPATH, '//input[@class="input_login login_btn"]')
# 错误信息提示
error_msg = (By.XPATH, '//div[@id="msg-box"]')

# -------------测试数据------------------------
userName = 13248231369
errorUsername = 132482313691
pwd = 1995030226
errorPwd = 111111
errorMsg = '用户名密码错误'
# -------------测试sql------------------------
