"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/09
@File   :Auto_selenium_id.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建webDriver 实例对象
webDriver = webdriver.Chrome()
webDriver.get(r'https://cdn2.byhy.net/files/selenium/test3.html')

# 清除文本框的内容：clear()方法
webDriver.find_element(By.ID,'input1').clear()
webDriver.find_element(By.ID,'input1').send_keys('yuerwen（文跃锐）')

webDriver.quit()


