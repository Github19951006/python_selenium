"""
@Project ：python_selenium 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/19
@File   :Auto_selenium_frame_title.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(5)

# 打开浏览器
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample3.html')


## 点击打开新窗口的链接
link = webDriver.find_element(By.TAG_NAME, "a")
link.click()

# wd.title属性是当前窗口的标题栏 文本
print(webDriver.title)

handles = webDriver.window_handles
for handle in handles:
	webDriver.switch_to.window(handle)
	if '必应' in webDriver.title:
		break
		
# 切换成功之后的title
print(webDriver.title)

webDriver.quit()

