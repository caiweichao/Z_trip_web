from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import random

driver = webdriver.Chrome()
driver.get('https://www.z-trip.cn')
driver.maximize_window()
old = driver.window_handles
print(old)
driver.find_element_by_xpath("//a[text()='立即登录']").click()
x = driver.window_handles  # 获取当前打开的所有窗口句柄 有序的最新打开的放最后
print(x)
WebDriverWait(driver, 10, 3).until(EC.new_window_is_opened(old))
driver.switch_to.window(x[-1])
driver.find_element_by_xpath('//input[@name="username"]').send_keys('13248231369')
driver.find_element_by_xpath('//input[@id="submitLogin"]').send_keys('1995030226')
driver.find_element_by_xpath('//input[@class="input_login login_btn"]').click()
# 找到设置的元素定位
time.sleep(2)
sz = driver.find_element_by_xpath('//div[@data-popup="popup-setting"]')
print(sz)
# 鼠标悬浮在设置上展开菜单
ActionChains(driver).move_to_element(sz).perform()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"- 职级标准设置")]')))
driver.find_element_by_xpath('//a[contains(text(),"- 职级标准设置")]').click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '''//input[@onclick="editEmpLevel('7021')"]''')))
driver.find_element_by_xpath('''//input[@onclick="editEmpLevel('7021')"]''').click()
time.sleep(1)
driver.find_element_by_xpath('//input[@onclick="submitEmpLevel()"]').click()
# 执行js语法
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@onclick="saveConfig()"]')))
# ele = driver.find_element_by_xpath('//input[@onclick="saveConfig()"]')
# driver.execute_script("arguments[0].scrollIntoView(false);", ele)
# time.sleep(3)
# ele1 =driver.find_element_by_xpath('//span[text()="是否允许预订国内机票"]')
# driver.execute_script("arguments[0].scrollIntoView(false);", ele1)
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# #iframe切换
# driver.switch_to.frame()
# #回到打开浏览器时的html页面'
# driver.switch_to.default_content()
# 处理select option
