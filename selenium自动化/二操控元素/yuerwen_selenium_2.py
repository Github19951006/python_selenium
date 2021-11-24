"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_2.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

web_file = Service(r'd:\webdrivers\chromedriver.exe')
webdriver_object = webdriver.Chrome(service=web_file)
# 设置等待时间
webdriver_object.implicitly_wait(5)
# 通过get方法  打开web网页
webdriver_object.get(r'https:baidu.com')
webdriver_object.find_element(By.ID,'kw').send_keys('文跃锐')
webdriver_object.find_element(By.ID,'su').click()

elemens_list = webdriver_object.find_elements(By.ID,'1')
print(elemens_list[1].get_attribute('innerHTML'))

# element = webdriver_object.find_elements(By.ID,'1')
# print(element[1].get_attribute('textContent'))
# for e in element:
# 	print(e[1].text)

# 获取文本框的信息
# value = webdriver_object.find_element(By.CLASS_NAME,'s_ipt').get_attribute('value')
# print(value)
webdriver_object.quit()