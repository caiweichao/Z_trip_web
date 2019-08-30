from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class homePage:
    def __init__(self, driver):
        self.driver = driver

    def isexit(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//i[@class="iconfont icon-userback"]')))
            return True
        except:
            return False
