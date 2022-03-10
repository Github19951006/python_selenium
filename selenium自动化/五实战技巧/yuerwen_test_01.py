"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/24
@File   :yuerwen_test_01.py
"""
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
# web_file = r'https://www.baidu.com/'
# wd.get(web_file)

web_file1 = r'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
wd.get(web_file1)

# 切换到iframe 对象中
wd.switch_to.frame('iframeResult')
# 实例化对象
action_chains_obj = ActionChains(wd)
# 调用actionChains对象的方法

# 1- 鼠标移动到某个元素  move_to_element()
# action_chains_obj.move_to_element(
# 	wd.find_element(By.CSS_SELECTOR,'#s-top-left   .s-top-more-btn')
# ).perform()

# 2- 拖拽到某个元素然后松开  drag_and_drop(被拖拽对象，目标对象)
source = wd.find_element(By.CSS_SELECTOR,'#draggable')
target = wd.find_element(By.CSS_SELECTOR,'#droppable')
action_chains_obj.drag_and_drop(source, target).perform()


# 关闭网页
# wd.quit()