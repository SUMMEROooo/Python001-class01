from scrapy import cmdline
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
print(dirpath)
# 添加环境变量
sys.path.append(dirpath) 
# 切换工作目录
os.chdir(dirpath)
# 启动爬虫,第三个参数为爬虫name
cmdline.execute('scrapy crawl maoyan'.split())