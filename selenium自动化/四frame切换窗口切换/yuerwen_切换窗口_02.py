"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/14
@File   :yuerwen_切换窗口_02.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 启动Chrome浏览器 驱动
webdriver_files = Service(r'd:\webdrivers\chromedriver.exe')
web_driver = webdriver.Chrome(service= webdriver_files)

# 打开指定web网页
web_files = r'http://cdn1.python3.vip/files/selenium/sample3.html'
web_driver.get(web_files)

# 点击按钮
web_driver.find_element(By.CSS_SELECTOR,'a').click()

# 注意：web_driver对象指向的还是老窗口，web_driver.title返回的结果还是旧的窗口title
# 获取当前网页的句柄
main_handle = web_driver.current_window_handle
print(web_driver.title)

# 切换到其他网页
for handle in web_driver.window_handles:
	# 先切换到该窗口
	web_driver.switch_to.window(handle)
	
	# 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
	# if '必应' in web_driver.title:
	# 	print(web_driver.title)
	# 	# 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
	# 	break
		
# 输出入文字
web_driver.find_element(By.CSS_SELECTOR,'#sb_form_q').send_keys('文跃锐')

web_driver.switch_to.window(main_handle)
web_driver.find_element(By.CSS_SELECTOR,'#outerbutton').click()