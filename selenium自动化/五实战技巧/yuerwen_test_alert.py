"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/31
@File   :yuerwen_test_alert.py
"""
# 警告提示类型的 alert
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

# 点击alert按钮
wd.find_element(By.ID,'b1').click()
# 获取弹窗的信息
print(wd.switch_to.alert.text)
# 关闭弹窗窗口（点击 OK 按钮）
wd.switch_to.alert.accept()

wd.quit()

