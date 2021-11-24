"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/18
@File   :yuerwen_selenium_wd_1.py
"""
# 导包
from selenium import webdriver
import time

# 创建WebDriver 实例对象 说明使用Chrome浏览器驱动
# WebDriver = webdriver.Chrome(chromedriver_files =
#                              Service(r'd:\webdrivers\chromedriver.exe'))  # 手动输入Chrome浏览器驱动地址路径
WebDriver = webdriver.Chrome()
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
WebDriver.get(r'http://www.baidu.com')

time.sleep(1)

WebDriver.quit()

