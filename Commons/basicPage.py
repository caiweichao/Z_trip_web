# 基类封装webdriver方法,方便调用,减少代码重复

from Commons.Logs import log
from Commons.LogManagement import LogManagement
from Commons import Contans
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import datetime


class BasicPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    # 等待元素可见
    def wait_element_visible(self, locator, timeout=Contans.basic_timeout,
                             pollinginterval=Contans.basic_Polling_Interval):
        log.info('等待元素: {}可见'.format(locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollinginterval).until(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info('元素已可见,共计等待:{}秒'.format(wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("等待元素超时,页面已经截图并且保存文件名:{}".format(tag_time))
            raise e
        except InvalidSelectorException as e:
            log.error("等待或定位表达式异常\n {}".format(e))

    # 等待元素存在
    def wait_element_exist(self, locator, timeout=Contans.basic_timeout,
                           pollinginterval=Contans.basic_Polling_Interval):
        log.info('等待元素: {}存在'.format(locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollinginterval).until(
                ec.presence_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info("元素已经存在,共计等待:{}秒".format(wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("等待元素超时,页面已经截图并且保存文件名:{}".format(tag_time))
            raise e
        except InvalidSelectorException as e:
            log.error("等待或定位表达式异常\n {}".format(e))

    # 等待元素不可见
    def wait_element_not_visible(self, locator, timeout=Contans.basic_timeout,
                                 pollinginterval=Contans.basic_Polling_Interval):
        log.info('等待元素: {}消失不可见'.format(locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollinginterval).until_not(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info("元素已经消失不见,共计等待:{}秒".format(wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("等待元素超时,页面已经截图并且保存文件名:{}".format(tag_time))
            raise e
        except InvalidSelectorException as e:
            log.error("等待或定位表达式异常\n {}".format(e))

    # 定位元素
    def find_element(self, model, locator, mode='visible'):
        """
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :return:
        """
        # 判断元素定位使用的是那种等待方式
        if mode == 'visible':
            self.wait_element_visible(locator)
        elif mode == 'notvisible':
            self.wait_element_not_visible(locator)
        elif mode == 'exist':
            self.wait_element_exist(locator)
        else:
            log.error('type参数传值异常,入参值为：{}'.format(mode))
        try:
            log.info('正在查找{}页面属性为: {} 的元素'.format(model, locator))
            # 元素定位传入动态参数
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("查找元素失败,页面已经截图并且保存文件名:{}".format(tag_time))
            raise e

    # 定位一组元素
    def find_elements(self, model, locator, mode='visible'):
        """
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        """
        # 判断元素定位使用的是那种等待方式
        if mode == 'visible':
            self.wait_element_visible(locator)
        elif mode == 'notvisible':
            self.wait_element_not_visible(locator)
        elif mode == 'exist':
            self.wait_element_exist(locator)
        else:
            log.error('type参数传值异常,入参值为：{}'.format(mode))
        try:
            log.info('正在查找{}页面属性为: {} 的元素'.format(model, locator))
            # 元素定位传入动态参数
            elements = self.driver.find_elements(*locator)
            return elements
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("查找元素失败,页面已经截图并且保存文件名:{}".format(tag_time))
            raise e

    # 点击元素
    def click_element(self, model, locator, mode='visible'):
        log.info('尝试点击:{}页面,属性为{}的元素'.format(model, locator))
        # 查找需要点击的元素
        element = self.find_element(model, locator, mode)
        try:
            log.info('点击操作:{}页面下的属性为: {}的元素'.format(model, locator))
            element.click()
        except Exception:
            log.error('页面{}的属性: {} 点击失败请检查'.format(model, locator))
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            raise

    # 输入文本内容
    def input_text(self):
        pass

    # 获取元素的文本内容

    # 句柄切换

    # 异常截图并且存储
    def save_webimg(self, tag_time):
        # 创建图片存储文件夹如果存在就不创建,并且删除七天之前的图片文件夹
        imgdir = LogManagement().get_log_dir(logs_path=Contans.pt_log)
        # 图片文件名称= 文件夹路径+模块名称_当前时间的时间戳.png
        imgPath = imgdir + "/{}".format(tag_time)
        try:
            # 尝试进行截图
            self.driver.save_screenshot(imgPath)
            log.info('截图成功,文件名称为: {} '.format(imgPath))
        except Exception as e:
            log.error('截图失败请检查\n{}'.format(e))
            raise e
        return imgPath


if __name__ == '__main__':
    pass
