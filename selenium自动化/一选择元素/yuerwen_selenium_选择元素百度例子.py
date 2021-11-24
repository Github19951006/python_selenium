"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/20
@File   :yuerwen_selenium_选择元素百度例子.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')
# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
webdriver_obj = webdriver.Chrome(service=webdriver_file)
# 设置最大等待时长为 10秒
webdriver_obj.implicitly_wait(5)

# 根据webdriver对象的get方法 打开指定的web地址
web_file = r'https://www.baidu.com'
webdriver_obj.get(web_file)

webdriver_obj.find_element(By.ID,'kw').send_keys('文跃锐')
webdriver_obj.find_element(By.ID,'su').click()

# 返回的是 WebElement 对象存放的 list
# 现在搜索结果在百度页面上，有2个ID为1 的元素，它是第2个
elemens_list = webdriver_obj.find_elements(By.ID,'1')
print(elemens_list[1].text)

