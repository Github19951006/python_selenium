"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/15
@File   :Auto_selenium_css_选择子元素.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(5)

# 打开web路径
web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
webDriver.get(web_file)

# 通过子节点 缩小范围来获取span 对象
inner21s = webDriver.find_elements(By.CSS_SELECTOR,'#container #inner11  span')
for inner in inner21s:
	print(inner.get_attribute('outerHTML'))

webDriver.quit()