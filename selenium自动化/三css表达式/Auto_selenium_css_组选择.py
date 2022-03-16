"""
@Project ：python_selenium 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/16
@File   :Auto_selenium_css_组选择.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome()

# 创建一个等待时间
webDriver.implicitly_wait(5)
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample1a.html')

elements  = webDriver.find_elements(By.CSS_SELECTOR,'#t1 span,#t2 p')
for e in elements:
	print(e.text)
	
webDriver.quit()