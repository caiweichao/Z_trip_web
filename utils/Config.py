import configparser
import os

from utils import Contans


# 创建实例
# 加载配置文件
# 根据section，option 来取到配置的值
class ConfigLoader:

    def __init__(self):
        # 创建实例
        self.conf = configparser.ConfigParser()
        # 加载配置文件
        self.conf.read(filenames=Contans.global_conf, encoding='utf-8')
        if self.get('env', 'profile') == 'PRO':
            self.conf.read(filenames=Contans.pro_conf, encoding='utf-8')
        elif self.get('env', 'profile') == 'SIT':
            self.conf.read(filenames=Contans.sit_conf, encoding='utf-8')
        elif self.get('env', 'profile') == 'UAT':
            self.conf.read(filenames=Contans.uat_conf, encoding='utf-8')

    def get(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.get(section, option)

    def getboolean(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getboolean(section, option)

    def getint(self, section, option):  # 返回str类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getint(section, option)

    def getfloat(self, section, option):  # 返回float类型的值
        # 根据section，option 来取到配置的值
        return self.conf.getfloat(section, option)

    def get_basic_conf(self):
        self.conf.read(filenames=Contans.global_conf, encoding='utf-8')
        return self.get('env', 'profile')

if __name__ == '__main__':
    X=ConfigLoader().get_basic_conf()
    print(X)