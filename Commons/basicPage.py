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
    def wait_element_visible(self, model, locator):
        log.info('等待页面:{}元素: {}可见'.format(model, locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info('页面{}上的元素{}已可见,共计等待:{}秒'.format(model, locator, wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("页面:{},等待元素可见{}超时".format(model, locator))
            raise e
        except InvalidSelectorException as e:
            log.error("页面:{},元素不可见或定位表达式:{}异常\n {}".format(model, locator, e))

    # 等待元素存在
    def wait_element_exist(self, model, locator):
        log.info('等待页面:{}元素: {}存在'.format(model, locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until(
                ec.presence_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info('页面{}上的元素{}已存在,共计等待:{}秒'.format(model, locator, wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("页面:{},等待元素存在{}超时".format(model, locator))
            raise e
        except InvalidSelectorException as e:
            log.error("页面:{},元素不存在或定位表达式:{}异常\n {}".format(model, locator, e))

    # 等待元素不可见
    def wait_element_not_visible(self, model, locator):
        log.info('等待页面:{}元素: {}不可见'.format(model, locator))
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until_not(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info('页面{}上的元素{}已不可见,共计等待:{}秒'.format(model, locator, wait_time))
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("页面:{},等待元素不可见{}超时".format(model, locator))
            raise e
        except InvalidSelectorException as e:
            log.error("页面:{},元素未不可见或定位表达式:{}异常\n {}".format(model, locator, e))

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
            log.error('定位{}页面的元素:{},type参数传值异常,入参值为：{}'.format(model, locator, mode))
        try:
            log.info('正在查找{}页面属性为: {} 的元素'.format(model, locator))
            # 元素定位传入动态参数
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            log.error("页面:{},定位元素:{}失败".format(model, locator))
            self.save_webimg(tag_time=tag_time)
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
            log.error('定位{}页面的元素:{},type参数传值异常,入参值为：{}'.format(model, locator, mode))
        try:
            log.info('正在查找{}页面属性为: {} 的元素'.format(model, locator))
            # 元素定位传入动态参数
            elements = self.driver.find_elements(*locator)
            return elements
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            log.error("页面:{},查找元素组:{}失败".format(model, locator))
            self.save_webimg(tag_time=tag_time)
            raise e

    # 将等待操作的元素移动到可见区域
    def make_element_visible(self, model, locator, element, alignment='false'):
        '''
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param alignment 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param element 需要可见的元素
        '''
        log.info('将{}页面的元素:{}移动至浏览器可见区域'.format(model, locator))
        # 将元素移动到可见区域
        try:
            self.driver.execute_script('arguments[0].scrollIntoView({0});'.format(alignment), element)
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error("{}页面的元素移动失败,页面已经截图并且保存文件名:{}}".format(model, tag_time))
            raise e

    # 点击元素
    def click_element(self, model, locator, mode='visible', make_ele_visible=False):
        log.info('尝试点击:{}页面,属性为{}的元素'.format(model, locator))
        # 查找需要点击的元素
        element = self.find_element(model, locator, mode)
        # 通过参数判断是否需要移动元素
        if make_ele_visible is True:
            # 代码执行比页面渲染速度快 这里放0.5秒等待页面渲染
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, element=element)
        try:
            log.info('点击操作:{}页面下的属性为: {}的元素'.format(model, locator))
            element.click()
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的属性: {} 点击失败'.format(model, locator))
            raise

    # 获取当前页面的句柄
    def get_handles(self):
        # 获取当前页面的句柄
        get_handle = self.driver.window_handles
        return get_handle

    # 浏览器页面切换--通过切换句柄实现切换到正在使用的页面上
    def swich_window(self, old_handle):
        # 智能等待最新的窗口出现
        WebDriverWait(self.driver, timeout=Contans.basic_timeout, poll_frequency=Contans.basic_Polling_Interval).until(
            ec.new_window_is_opened(old_handle))
        # 调用获取句柄的方法拿到最新打开的标签页的句柄
        new = self.get_handles()
        # 切换到最新页面因为时最新所以直接使用下标 -1 就行
        self.driver.switch_to.window(new[-1])

    # 输入文本内容
    def input_text(self, model, locator, content, mode='visible', make_ele_visible=False):
        log.info('尝试在:{}页面的:{}元素中输入文本内容{}'.format(model, locator, content))
        element = self.find_element(model, locator, mode)
        if make_ele_visible is True:
            # 代码执行比页面渲染速度快 这里放0.5秒等待页面渲染
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, element=element)
        try:
            log.info('输入操作:{}页面下的属性为:{}的元素,输入内容为'.format(model, locator, content))
            element.send_keys(content)
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的属性: {} 输入操作失败'.format(model, locator))
            raise

    # 获取元素的文本内容

    # 异常截图并且存储
    def save_webimg(self, tag_time):
        # 创建图片存储文件夹如果存在就不创建,并且删除七天之前的图片文件夹
        imgdir = LogManagement().get_log_dir(logs_path=Contans.pt_log)
        # 图片文件名称= 文件夹路径+模块名称_当前时间的时间戳.png
        img_path = imgdir + "/{}".format(tag_time)
        try:
            # 尝试进行截图
            self.driver.save_screenshot(img_path)
            log.info('截图成功,文件名称为: {} '.format(img_path))
        except Exception as e:
            log.error('截图失败请检查\n{}'.format(e))
            raise e
        return img_path


if __name__ == '__main__':
    pass
