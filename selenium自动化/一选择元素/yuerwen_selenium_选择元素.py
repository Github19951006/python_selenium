"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/19
@File   :yuerwen_selenium_选择元素.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

file = r'd:\webdrivers\chromedriver.exe'
webdriver_object = webdriver.Chrome(file)

webdriver_object.get(r'http://127.0.0.1/mgr/sign.html')

# element = webdriver_object.find_element_by_id('username')  不赞成使用
# 根据ID选择元素，返回的就是该元素对应的webdriver对象
element= webdriver_object.find_element(By.ID, 'username').send_keys('byhy')
# 输入文本
# element.send_keys('byhy')
element = webdriver_object.find_element(By.ID,'password').send_keys('88888888')


# webdriver_object.find_element_by_class_name('col-xs-12').click() 未来不赞成使用
# webdriver_object.find_element(By.CLASS_NAME,'col-xs-12').click()
webdriver_object.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
