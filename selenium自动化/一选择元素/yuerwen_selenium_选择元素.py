"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/19
@File   :yuerwen_selenium_选择元素.py
"""
# selenium的八种元素定位方式有：id、name、class_name、tag_name、link_text、partial_link_text、xpath、css_selector。
# 第一种：id

from selenium import webdriver
from selenium.webdriver.common.by import By

# file = r'd:\webdrivers\chromedriver.exe'
# 创建webDriver 实例对象 驱动Chrome浏览器（省略了Chrome驱动器的地址，配置在系统环境path变量中）
webDriver = webdriver.Chrome()

webDriver.get(r'http://127.0.0.1/mgr/sign.html')

# element = webdriver_object.find_element_by_id('username')  不赞成使用
# 根据ID选择元素，返回的就是该元素对应的webdriver对象
element = webDriver.find_element(By.ID, 'username').send_keys('byhy')
# 输入文本
# element.send_keys('byhy')
element = webDriver.find_element(By.ID,'password').send_keys('88888888')


# webdriver_object.find_element_by_class_name('col-xs-12').click() 未来不赞成使用
# webdriver_object.find_element(By.CLASS_NAME,'col-xs-12').click()
webDriver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
