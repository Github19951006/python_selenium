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
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample1.html')

elemet_plant = webDriver.find_element(By.CLASS_NAME,'plant')
elemets_animal = webDriver.find_elements(By.CLASS_NAME,'animal')
print(f'植物：{elemet_plant.text}')

for element in elemets_animal:
	print(f'动物：{element.text}')



webDriver.quit()


