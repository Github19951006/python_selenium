"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/28
@File   :yuerwen_test_03.py
"""
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 打开指定网页地址
web_files = r'http://sahitest.com/demo/dragDropMooTools.htm'
wd.get(web_files)

# 被拖拽的元素
source_dragger = wd.find_element(By.CSS_SELECTOR,'#dragger')
target_items = wd.find_elements(By.CSS_SELECTOR,'body .item')

# 创建一个actionChains类对象
ac = ActionChains(wd)
#  drag_and_drop(source, target) ——拖拽到某个元素然后松开
ac.drag_and_drop(source_dragger,target_items[1]).perform()

# 关闭浏览器
wd.quit()