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
webDriver.get(r'http://www.baidu.com')

# webDriver.find_element(By.ID,'kw').send_keys('文跃锐')
# webDriver.find_element(By.ID,'kw').click()


# webDriver.find_element(By.ID,'su').click()

webDriver.find_element(By.LINK_TEXT,'新闻').click()

# webDriver.quit()

