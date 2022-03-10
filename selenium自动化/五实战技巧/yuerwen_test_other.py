"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/31
@File   :yuerwen_test_other.py
"""
# 警告提示类型的 prompt（提示输入）
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 打开指定网页地址
web_files = r'http://cdn1.python3.vip/files/selenium/test4.html'
wd.get(web_files)

# 点击Confirm按钮
wd.find_element(By.ID,'b3').click()

# 获取alert 对象
alert_element = wd.switch_to.alert

# 获取alert 对象
alert_element = wd.switch_to.alert

# 点击确认下按钮
alert_element.accept()

# 获取窗口大小
print(wd.get_window_size())
# 改变窗口大小
wd.set_window_size(440, 330)

# 获取当前窗口标题
print(wd.title)

# 获取当前窗口URL地址
print(wd.current_url)

# 截图
wd.get_screenshot_as_file('1.png')
input(' ')
# 关闭网页
# wd.quit()1
