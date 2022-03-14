"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_1.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

# 创建等待时间
wd.implicitly_wait(5)

web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
wd.get(web_file)

print(wd.find_element(By.CSS_SELECTOR,'.animal').text)

wd.quit()