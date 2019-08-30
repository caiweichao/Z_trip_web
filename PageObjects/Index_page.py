from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class indexpage:
    def __init__(self, driver):
        self.driver = driver

    def click(self):
        self.old = self.driver.window_handles
        self.driver.find_element_by_xpath("//a[text()='立即登录']").click()
        # 获取当前打开的所有窗口句柄 有序的最新打开的放最后
        WebDriverWait(self.driver, 10, 3).until(EC.new_window_is_opened(self.old))
        self.x = self.driver.window_handles
        self.driver.switch_to.window(self.x[-1])
