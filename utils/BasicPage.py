# 基类封装webdriver方法,方便调用,减少代码重复

from utils.Logs import log
from utils.LogManagement import LogManagement
from utils import Contans
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
import datetime
import allure


class BasicPage:
    def __init__(self, driver):
        self.driver = driver

    """
    等待元素可见
    :param model: 
    :param locator: 
    :return: 
    """
    def wait_element_visible(self, model, locator):

        log.info(f'等待页面:{model}元素: {locator}可见')
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info(f'页面：{model}上的元素{locator}已可见,共计等待:{wait_time}秒')
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error(f"页面:{model},等待元素可见{locator}超时")
            raise e
        except InvalidSelectorException as e:
            log.error(f"页面:{model},元素不可见或定位表达式:{locator}异常\n {e}")

    # 等待元素存在
    def wait_element_exist(self, model, locator):
        log.info(f'等待页面:{model}元素: {locator}存在')
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            # 默认超时等待时间为30秒,间隔0.5秒轮询一次可以根据配置文件修改超时时间和轮询时间
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until(
                ec.presence_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info(f'页面：{model}上的元素{locator}已存在,共计等待:{wait_time}秒')
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error(f"页面:{model},等待元素存在{locator}超时")
            raise e
        except InvalidSelectorException as e:
            log.error(f"页面:{model},元素不存在或定位表达式:{locator}异常\n {e}")

    # 等待元素不可见
    def wait_element_not_visible(self, model, locator):
        log.info(f'等待页面:{model}元素: {locator}不可见')
        try:
            # 获取开始等待时间具体到秒
            start_time = datetime.datetime.now().second
            WebDriverWait(self.driver, timeout=Contans.basic_timeout,
                          poll_frequency=Contans.basic_Polling_Interval).until_not(
                ec.visibility_of_element_located(locator))
            # 计算共计等待时间
            wait_time = datetime.datetime.now().second - start_time
            log.info(f'页面{model}上的元素{locator}已不可见,共计等待:{wait_time}秒')
        except TimeoutException as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error(f"页面:{model},等待元素不可见{locator}超时")
            raise e
        except InvalidSelectorException as e:
            log.error(f"页面:{model},元素未不可见或定位表达式:{locator}异常\n {e}")

    # 定位元素
    def find_element(self, model, locator, mode='visible'):
        """
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :return: 返回获取到的元素定位
        """
        # 判断元素定位使用的是那种等待方式
        if mode == 'visible':
            self.wait_element_visible(model, locator)
        elif mode == 'notvisible':
            self.wait_element_not_visible(model, locator)
        elif mode == 'exist':
            self.wait_element_exist(model, locator)
        else:
            log.error(f'定位{model}页面的元素:{locator},type参数传值异常,入参值为：{mode}')
        try:
            log.info(f'正在查找{model}页面属性为: {locator} 的元素')
            # 元素定位传入动态参数
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            log.error(f"页面:{model},定位元素:{locator}locator失败")
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
            self.wait_element_visible(model, locator)
        elif mode == 'notvisible':
            self.wait_element_not_visible(model, locator)
        elif mode == 'exist':
            self.wait_element_exist(model, locator)
        else:
            log.error(f'定位{model}页面的元素:{locator},type参数传值异常,入参值为：{mode}')
        try:
            log.info(f'正在查找{model}页面属性为: {locator} 的元素')
            # 元素定位传入动态参数
            elements = self.driver.find_elements(*locator)
            return elements
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error(f"页面:{model},查找元素组:{locator}失败")
            raise e

    # 将等待操作的元素移动到可见区域
    def make_element_visible(self, model, locator, element, alignment='false'):
        '''
        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param alignment 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param element 需要可见的元素
        '''
        log.info(f'将{model}页面的元素:{locator}移动至浏览器可见区域')
        # 将元素移动到可见区域
        try:
            self.driver.execute_script('arguments[0].scrollIntoView({0});'.format(alignment), element)
        except Exception as e:
            # 获取超时时间戳
            tag_time = time.time()
            # 截图并且保存
            self.save_webimg(tag_time=tag_time)
            log.error(f"{model}页面的元素:{locator}移动失败")
            raise e

    # 点击元素
    def click_element(self, model, locator, mode='visible', alignment='false', make_ele_visible=False):
        '''

        :param model: 传参定位的是哪个页面 字符串形式
        :param locator: 元素的定位表达式 例:(By.xx,'定位表达式')
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :param alignment 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :return: 方法无返回值
        '''
        log.info('尝试点击:{}页面,属性为{}的元素'.format(model, locator))
        # 查找需要点击的元素
        element = self.find_element(model, locator, mode)
        # 通过参数判断是否需要移动元素
        if make_ele_visible is True:
            # 代码执行比页面渲染速度快 这里放0.5秒等待页面渲染
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, element=element, alignment=alignment)
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
        '''
        :return: 方法返回值当前获取到的句柄值
        '''
        # 获取当前页面的句柄
        handles = self.driver.window_handles
        return handles

    # 浏览器页面切换--通过切换句柄实现切换到正在使用的页面上
    def swich_window(self, old_handle):
        '''
        :param old_handle: 传入之前获取的句柄的值
        :return:
        '''
        # 智能等待最新的窗口出现
        WebDriverWait(self.driver, timeout=Contans.basic_timeout, poll_frequency=Contans.basic_Polling_Interval).until(
            ec.new_window_is_opened(old_handle))
        # 调用获取句柄的方法拿到最新打开的标签页的句柄
        new = self.get_handles()
        # 切换到最新页面因为时最新所以直接使用下标 -1 就行
        self.driver.switch_to.window(new[-1])

    # 输入文本内容
    def input_text(self, model, locator, content, mode='visible', alignment='false', make_ele_visible=False):
        '''

        :param model: 传入字符串 代表那个页面
        :param locator: 传入元素定位表达式
        :param content: 传入输入的文本内容
        :param mode:  visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 方法无返回值
        '''
        log.info('尝试在:{}页面的:{}元素中输入文本内容{}'.format(model, locator, content))
        element = self.find_element(model, locator, mode)
        if make_ele_visible is True:
            # 代码执行比页面渲染速度快 这里放0.5秒等待页面渲染
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, alignment=alignment, element=element)
        try:
            log.info('输入操作:{}页面下的属性为:{}的元素,输入内容为{}'.format(model, locator, content))
            element.send_keys(content)
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的属性: {} 输入操作失败'.format(model, locator))
            raise

    # 获取元素的属性
    def get_element_attr(self, model, locator, attribute='textContent', mode='visible', alignment='false',
                         make_ele_visible=False):
        '''

        :param model: 传入字符串 代表那个页面
        :param locator: 传入元素定位表达式
        :param attribute: 默认 'textContent' 获取文本内容 'innerHTML' 获取元素内的全部HTML 'outerHTML'  获取包含选中元素的HTML
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 返回获取到的元素属性内容
        '''
        log.info('尝试在:{}页面的:{}元素中获取元素属性'.format(model, locator))
        element = self.find_element(model=model, locator=locator, mode=mode)
        if make_ele_visible is True:
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, alignment=alignment, element=element)
        try:
            log.info('属性获取操作:{}页面下的属性为:{}的元素的{}'.format(model, locator, attribute))
            return element.get_attribute(attribute)
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的属性: {} 获取属性操作失败'.format(model, locator))
            raise

    # 获取元素的文本内容
    def get_element_text(self, model, locator, mode='visible', alignment='false', make_ele_visible=False):
        '''

        :param model: 传入字符串 代表那个页面
        :param locator:  传入元素定位表达式
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 返回获取到的元素文本内容
        '''
        log.info('尝试在:{}页面的:{}元素中获取文本内容'.format(model, locator))
        element = self.find_element(model=model, locator=locator, mode=mode)
        if make_ele_visible is True:
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, alignment=alignment, element=element)
        try:
            log.info('文本获取操作:{}页面下的属性为:{}的元素的文本内容'.format(model, locator))
            return element.text
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的元素: {} 获取文本操作失败'.format(model, locator))
            raise

    # 复选框内容点击
    def click_radios(self, model, locator, method, amount=None, mode='visible', alignment='false',
                     make_ele_visible=False):
        '''

        :param model: 传入字符串 代表那个页面
        :param locator: 传入元素定位表达式
        :param mode:  visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param amount: 传入复选项的数量 例子如果是3个选项就传入3
        :param method: 选择对应的内容选择方式 all 点击复选框的全部内容 random 随机点击复选框的中的某一个选项 assign点击指定的某个复选项
        :param alignment: 默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        :return: 全了全部点击的，其他返回被点击的元素
        '''
        # 定位到复选框一定是一组元素
        log.info('尝试在:{}页面的:{}元素上定位单选框'.format(model, locator))
        elements = self.find_elements(model=model, locator=locator, mode=mode)
        if make_ele_visible is True:
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, alignment=alignment, element=elements)
        try:
            log.info('点击方式为：{}'.format(method))
            if method == 'all':
                # 点击复选项中每一个元素
                for ele in elements:
                    ele.click()
            # 随机点击复选项中的某一个内容
            elif method == 'random':
                # 导入随机数包
                import random
                # 生成指定范围之内的随机数作为需要点击的radio
                num = random.randint(0, amount - 1)
                element = elements[num].click()
                # 返回被点击的元素
                return element
            # 点击复选框中指定位置的选项
            elif method == 'assign':
                element = elements[amount - 1].click()
                return element
            else:
                log.error('点击方式输入错误，请检查')
        except Exception as e:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的元素: {} 复选框点击操作失败'.format(model, locator))
            raise e

    # 判断元素是否勾选
    def element_is_selected(self, elenmet):
        # 用于校验返回的是布尔值 选中是Ture 没有选择是False
        return elenmet.is_selected()

    # 选择下拉菜单中的内容
    def select_contents_menu(self, model, locator, text, mode='visible', alignment='false',
                             make_ele_visible=False):
        '''

        :param model: 传入字符串 代表那个页面
        :param locator: 传入元素定位表达式
        :param text: 出入下拉列表需要选择的内容
        :param mode: visible(元素可见),notvisible(元素消失不可见), exist(元素存在)
        :param alignment:  默认对其方式是元素和当前页面的底部对齐，可以传 alignment=''表示和顶部对齐
        :param make_ele_visible: 这里是布尔值 传入True 表示需要让元素滚动到页面可见区域 False 表示不用
        '''
        log.info('尝试选择下拉菜单{}，内容为{}'.format(locator, text))
        element = self.find_element(model, locator, mode)
        option = []
        if make_ele_visible is True:
            time.sleep(0.5)
            self.make_element_visible(model=model, locator=locator, alignment=alignment, element=element)
        try:
            # 获取下拉列表的内容
            options = element.find_elements_by_tag_name('option')
            for value in options:
                option.append(value)
            if text in option:
                Select(element).select_by_visible_text(text)
            else:
                log.error('选项:{}不在下拉列表之中请检查'.format(text))
        except Exception:
            # 获取点击失败时候的时间戳并且截图
            tag_time = time.time()
            self.save_webimg(tag_time)
            log.error('页面{}的元素: {} 下拉框操作失败请检查'.format(model, locator))
            raise

    # 处理页面的alert
    def dispose_alert(self, action):
        '''
        :param action: 参数为 accept 点击alert的确定 dismiss点击alert的取消
        :return: 返回alert的文本内容 可能有些用例需要用这个参数去校验
        '''
        # 等待alert出现再去操作
        WebDriverWait(self.driver, Contans.basic_timeout, Contans.basic_Polling_Interval).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        # 尝试点击alert
        try:
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            return alert.text
        except Exception as e:
            log.error('alert 处理参数错误请检查')
            raise e

    # 异常截图并且存储
    def save_webimg(self, tag_time):
        # 创建图片存储文件夹如果存在就不创建,并且删除七天之前的图片文件夹
        imgdir = LogManagement().get_log_dir(logs_path=Contans.pt_error_log)
        # 图片文件名称= 文件夹路径+模块名称_当前时间的时间戳.png
        img_path = imgdir + "/{}.png".format(tag_time)
        try:
            # 尝试进行截图
            self.driver.save_screenshot(img_path)
            log.error('截图成功,文件名称为: {} '.format(img_path))
        except Exception as e:
            log.error('截图失败请检查\n{}'.format(e))
            raise e
        return img_path

    # 用例执行完毕截图
    def save_img_case(self):
        with allure.step('执行结果'):
            # 创建图片存储文件夹如果存在就不创建,并且删除七天之前的图片文件夹
            img_dir = LogManagement().get_log_dir(logs_path=Contans.pt_report_log)
            # 图片地址构建
            img_path = img_dir + "/{}.png".format(time.time())
            # 尝试截图
            try:
                # 尝试截图,等待一秒保证图片正确加载
                time.sleep(1)
                self.driver.save_screenshot(img_path)
                log.info('用例执行完成，截图成功,文件名称为: {} '.format(img_path))
                return img_path
            except Exception as e:
                log.error('截图失败请检查\n{}'.format(e))
                raise e

    def allure_img(self):
        try:
            log.info('尝试将测试结果图片存入allure报告')
            # 读取测试结果图片
            file = open(self.save_img_case(), 'rb').read()
            # 将图片加入allure报告中
            allure.attach(file, '测试结果截图', allure.attachment_type.PNG)
        except Exception as e:
            log.error('图片未能成功加入allure请检查\n{}'.format(e))
            raise e


if __name__ == '__main__':
    pass
