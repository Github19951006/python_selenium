"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/20
@File   :yuerwen_selenium_选择元素2.py
"""
# 练习例子
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建 webdriver 实例对象，指明使用Chrome浏览器驱动
# webdriver_file = r'd:\webdrivers\chromedriver.exe'

# Google浏览器的驱动器的地址
webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')
# 创建webdriver实例对象 说明使用Chrome浏览器驱动
wb_object = webdriver.Chrome(webdriver_file)

# webdriver 实例对象的get方法  让浏览器打开指定的网址
sample1_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
wb_object.get(sample1_file)

# find_elements(By.CLASS_NAME,'名称')  获取class属性的元素
# list_elements = wb_object.find_elements(By.CLASS_NAME,'animal')

# By.TAG_NAME:根据元素的标签获取
list_elements = wb_object.find_elements(By.TAG_NAME, 'span')

for elemen in list_elements:
	print(elemen.text)
	