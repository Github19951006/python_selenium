"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/15
@File   :Auto_selenium_css_2.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(5)

# 打开web路径
web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
webDriver.get(web_file)

inner21 = webDriver.find_element(By.CSS_SELECTOR,'#container #inner21')
print(inner21.find_element(By.CSS_SELECTOR,'span').text)

webDriver.quit()