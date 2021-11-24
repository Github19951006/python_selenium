"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_1.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

web_file = Service(r'd:\webdrivers\chromedriver.exe')
webdriver_object = webdriver.Chrome(service=web_file)
# 设置等待时间
webdriver_object.implicitly_wait(5)
# 通过get方法  打开web网页
webdriver_object.get(r'http://127.0.0.1/mgr/sign.html')

# 根据ID选择元素，返回的就是该元素对应的webdriver对象
webdriver_object.find_element(By.ID, 'username').send_keys('byhy')
# 输入文本
# element.send_keys('byhy')
webdriver_object.find_element(By.ID,'password').send_keys('88888888')
# 点击
webdriver_object.find_element(By.CLASS_NAME,'btn-primary').click()

# print(webdriver_object.get_attribute('onclick'))
# webdriver_object.quit()