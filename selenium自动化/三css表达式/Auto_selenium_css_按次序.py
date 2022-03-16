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
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample1b.html')

# 父元素的第n个子节点
span_element = webDriver.find_elements(By.CSS_SELECTOR,':nth-child(2)')
# for e in span_element:
	# print(e.get_attribute('outerHTML'))

# 父元素的倒数第n个子节点
span_element = webDriver.find_element(By.CSS_SELECTOR,'#t2 :nth-last-child(2)')
# print(span_element.text)

# 父元素的第几个某类型的子节点 nth-of-type
span_s = webDriver.find_elements(By.CSS_SELECTOR,':nth-of-type(1)')
for e in span_s:
	print(e.get_attribute('outerHTML'))
	print('-------------')

webDriver.quit()