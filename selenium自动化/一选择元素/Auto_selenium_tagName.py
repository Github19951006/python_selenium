"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/09
@File   :Auto_selenium_className.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建webDriver 实例对象
webDriver = webdriver.Chrome()
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample1.html')

elemets = webDriver.find_elements(By.TAG_NAME,'div')
for element in elemets:
	print(f'{element.text}')

webDriver.quit()


