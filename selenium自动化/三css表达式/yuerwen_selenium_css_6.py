"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_6.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://cdn1.python3.vip/files/selenium/sample1b.html'
wd.get(web_file)
# 选择子节点
# :nth-child(2) : 根据位置选择的
# 	:nth-last-child(2) 倒序选择
# :nth-of-type(2) : 根据类型选择
# 	:nth-last-of-type(2) 倒序选择
'''
奇数节点和偶数节点
奇数：odd
例如:p:nth-child(odd)
偶数：even
例如:p:nth-child(even)

'''
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
for e in elements:
	print(e.text)
	
print('-----------------------------')
elements = wd.find_elements(By.CSS_SELECTOR, '#t2 p:nth-of-type(2)')
for e in elements:
	print(e.text)
	
print('-----------------------------')
elements = wd.find_elements(By.CSS_SELECTOR, '#t2 span:nth-last-of-type(1)')
for e in elements:
	print(e.text)
	
print('-------------兄弟节点选择----------------')
'''
兄弟节点选择：
1、相邻兄弟节点：用加号 +
例如：(选择ID = t 和p相邻的span标签) #t p + span

2、后续相邻所有兄弟节点：波浪号 ~
例如：(选择ID = t 和p后续相邻的所有span标签) #t p ~ span
'''
print('-------------相邻兄弟节点：用加号 +----------------')
element = wd.find_element(By.CSS_SELECTOR, '#t2 span + p')
print(element.text)
	
print('-------------后续相邻所有兄弟节点：波浪号 ~----------------')

elements = wd.find_elements(By.CSS_SELECTOR, '#t2 span ~ p')
for e in elements:
	print(e.text)

# 关闭浏览器
wd.quit()