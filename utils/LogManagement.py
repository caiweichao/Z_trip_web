# 日志文件管理类
# 日志文件的创建以及定时删除日志文件

import os
import time
import shutil
from utils import Contans


class LogManagement:
    def get_current_day(self):  # 获取当天
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def get_log_dir(self,logs_path):  # 获取当天的日志存放目录
        log_dir = os.path.join(logs_path, self.get_current_day())
        if not os.path.isdir(log_dir):  # 判断是否存在
            os.makedirs(log_dir)  # 不存在就创建
            # 删除7天之前的全部日志文件 ,放这里减少调用提升代码性能
            self.delect_log_dir(logs_path=logs_path)
        return log_dir  # 存在就直接返回

    def delect_log_dir(self, logs_path):  # 删除n天之前的全部日志文件
        folders = os.listdir(logs_path)
        # 循环指定路径取出指定路径下全部的文件夹名称
        for folder in folders:
            # 判断文件夹是不是七天之前创建的如果是就删除
            if int(folder) < int(self.get_current_day()) - Contans.log_time:
                shutil.rmtree(os.path.join(logs_path, folder))
if __name__ == '__main__':
    pass