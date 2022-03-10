"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_1.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
wd.get(web_file)

w = wd.find_element(By.CSS_SELECTOR,'.animal').get_attribute('outerHTML')
print(w)
wd.quit()