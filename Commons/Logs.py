from Commons import Contans
import logging
import os
import time
import shutil

'''
#日志记录--记录用例名称，用例数据，用例返回值输出进入info文件
#日志记录--error日志进入进入error文件
#日志记录--debug信息输出到控制台
'''

# 定义一个日志收集器
logger = logging.getLogger('Log')
# # 输出日志级别，最低级别低于DEBUG 不输出不记录
logger.setLevel('DEBUG')


def set_handler(levels):
    if levels == 'error':  # 判断如果是error就添加error的handler
        logger.addHandler(log.error_handle)
    else:  # 其他添加到infohandler
        logger.addHandler(log.handler)
    logger.addHandler(log.ch)  # 全部输出到console
    # logger.addHandler(Log.report_handler)  # 全部输出到report


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(log.error_handle)
    else:
        logger.removeHandler(log.handler)

    logger.removeHandler(log.ch)
    # logger.addHandler(Log.report_handler)


def get_log_dir():  # 获取当天的日志存放目录
    log_dir = os.path.join(Contans.text_log, get_current_day())
    if not os.path.isdir(log_dir):  # 判断是否存在
        os.makedirs(log_dir)  # 不存在就创建
        # 删除7天之前的全部日志文件 ,放这里减少调用提升代码性能
        delect_log_dir(logs_path=Contans.text_log)
    return log_dir  # 存在就直接返回


def delect_log_dir(logs_path):  # 删除n天之前的全部日志文件
    folders = os.listdir(logs_path)
    # 循环指定路径取出指定路径下全部的文件夹名称
    for folder in folders:
        # 判断文件夹是不是七天之前创建的如果是就删除
        if int(folder) < int(get_current_day()) - Contans.log_time:
            shutil.rmtree(os.path.join(logs_path, folder))


def get_current_day():  # 获取当天
    return time.strftime('%Y%m%d', time.localtime(time.time()))


class log:
    log_dir = get_log_dir()
    # 指定输出文件
    log_file = os.path.join(log_dir, 'info.log')
    error_file = os.path.join(log_dir, 'error.log')

    # 设置日志输出格式
    formatter = logging.Formatter(Contans.formatter)
    # 指定输出渠道
    # 控制台输出
    ch = logging.StreamHandler()
    ch.setLevel('ERROR')
    ch.setFormatter(formatter)

    # INFO文件输出
    handler = logging.FileHandler(filename=log_file, encoding='utf-8')
    handler.setLevel('INFO')
    handler.setFormatter(formatter)

    # 错误文件输出
    error_handle = logging.FileHandler(filename=error_file, encoding='utf-8')
    error_handle.setLevel('ERROR')
    error_handle.setFormatter(formatter)

    # 报表日志输出 改为使用allure
    # report_handler = logging.StreamHandler(HTMLTestRunnerNew.stdout_redirector)
    # report_handler.setLevel('INFO')
    # report_handler.setFormatter(formatter)

    @staticmethod
    def debug(msg):
        set_handler('debug')
        logger.debug(msg)
        remove_handler('debug')

    @staticmethod
    def info(msg):
        set_handler('info')
        logger.info(msg)
        remove_handler('info')

    @staticmethod
    def error(msg):
        set_handler('error')
        logger.error(msg, exc_info=True)  # 同时输出异常信息
        remove_handler('error')


if __name__ == '__main__':
    pass
