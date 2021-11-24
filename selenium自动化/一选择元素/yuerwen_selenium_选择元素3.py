"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/20
@File   :yuerwen_selenium_选择元素3.py
"""
'''
区分：WebDriver 对象 和 WebElement 对象
WebDriver 对象 ：选择的元素对象范围是 整个web 页面
WebElement 对象 ：选择的元素对象范围是 该元素的内部。
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')
# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
webdriver_obj = webdriver.Chrome(service=webdriver_file)
# 根据webdriver对象的get方法 打开指定的web地址
web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
webdriver_obj.get(web_file)

# WebElement 对象 ：选择的元素对象范围是 该元素的内部。
web_element = webdriver_obj.find_element(By.ID,'container')
span = web_element.find_elements(By.TAG_NAME,'span')
for element in span:
	print(element.text)
	
print('---------------------------------------------------')

# WebDriver 对象 ：选择的元素对象范围是 整个web 页面
web_element = webdriver_obj.find_element(By.ID,'container')
span = webdriver_obj.find_elements(By.TAG_NAME,'span')
for element in span:
	print(element.text)
