"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/13
@File   :yuerwen_frame_01.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 启动Chrome浏览器 驱动
webdriver_files = Service(r'd:\webdrivers\chromedriver.exe')
web_driver = webdriver.Chrome(service= webdriver_files)

# 创建等待时间
web_driver.implicitly_wait(5)

# 打开指定web网页
web_files = r'http://cdn1.python3.vip/files/selenium/sample2.html'
web_driver.get(web_files)

# 说明切换到iframe的操作范围
web_driver.switch_to.frame('innerFrame')

# 如果iframe没有 id 和 name都没有的时候 要用element对象
# iframe_element = web_driver.find_element(By.CSS_SELECTOR,'iframe[src="sample1.html"]')
# web_driver.switch_to.frame(iframe_element)

# 操作元素的定位
plant_elements = web_driver.find_elements(By.CSS_SELECTOR,'.plant')
for e in plant_elements:
	print(e.get_attribute('outerHTML'))


# 切换到iframe外面的操作
web_driver.switch_to.default_content()
# 点击外部按钮
for i in range(10):
	web_driver.find_element(By.CSS_SELECTOR,'#outerbutton').click()

# 获取 点击了外部按钮 的回调
add_li_elements = web_driver.find_elements(By.CSS_SELECTOR,'#add li')
for li in add_li_elements:
	print(li.text)

# 关闭浏览器
web_driver.quit()