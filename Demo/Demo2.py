import os
import shutil
import time
from Commons.Contans import *
#删除文件夹
#shutil.rmtree('D:\Python_project\Z_trip_web\Logs\TextLog\\20190828')
ban = []
bag = os.listdir(text_log)
print(bag)
now = time.strftime('%Y%m%d', time.localtime(time.time()))
for log_file in bag:

    if int(log_file) < int(now)-20:
        shutil.rmtree(os.path.join(text_log,log_file))