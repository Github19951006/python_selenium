"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/09
@File   :Auto_selenium_className.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建webDriver 实例对象
webDriver = webdriver.Chrome()
# 指定打开的网址
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample1.html')

# 通过ID选择器  tag_name 选择器
elemet = webDriver.find_element(By.ID,'container')
elemets = elemet.find_elements(By.TAG_NAME,'div')

# elements 对象是存储在list中，遍历取出
for element in elemets:
	print(f'{element.text}')
	
# 关闭浏览器
# webDriver.quit()


