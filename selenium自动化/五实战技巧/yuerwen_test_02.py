"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/28
@File   :yuerwen_test_02.py
"""
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 打开指定网页地址
web_files = r'http://sahitest.com/demo/mouseover.htm'
wd.get(web_files)

Write_on_hover_element = wd.find_element(By.CSS_SELECTOR,'input[value="Write on hover"]')
Blank_on_hoverelement = wd.find_element(By.CSS_SELECTOR,'input[value="Blank on hover"]')
Kamlesh = wd.find_element(By.CSS_SELECTOR,'a[href="x"]')

# 创建一个actionChains类对象
ac = ActionChains(wd)
t1_element = wd.find_element(By.NAME,'t1')

# -- 链式写法
# ac.move_to_element(Write_on_hover_element).\
# 	move_to_element(Blank_on_hoverelement).move_to_element(Kamlesh).perform()

# -- 分布式写法
# - move_to_element() 鼠标移动到某个元素
ac.move_to_element(
	wd.find_element(By.CSS_SELECTOR,'input[value="Write on hover"]')
).perform()

ac.move_to_element(
	wd.find_element(By.CSS_SELECTOR,'input[value="Blank on hover"]')
).perform()

ac.move_to_element(
	wd.find_element(By.CSS_SELECTOR,'a[href="x"]')
).perform()

# - move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
# 这种使用位置关系来移动鼠标，几乎用不到
ac.move_by_offset(10, 50).perform()
print(t1_element.get_attribute('value'))



# 关闭浏览器
wd.quit()