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

# 获取动物类 的动物名称
animals = wd.find_elements(By.CSS_SELECTOR,'.animal')
animal_list = [animal.text for animal in animals]
print(animal_list) # ['狮子', '老虎', '山羊']

wd.quit()