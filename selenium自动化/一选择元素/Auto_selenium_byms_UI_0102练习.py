"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2021/11/19
@File   :yuerwen_selenium_选择元素.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


webDriver = webdriver.Chrome()
webDriver.get(r'http://127.0.0.1/mgr/sign.html')

# 登录
# 根据ID选择元素，返回的就是该元素对应的webdriver对象
element = webDriver.find_element(By.ID, 'username').send_keys('byhy')
element = webDriver.find_element(By.ID,'password').send_keys('88888888')
webDriver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

# 缓存1s
time.sleep(1)

# 获取左侧菜单，点击客户按钮
menu_element = webDriver.find_element(By.CLASS_NAME,'sidebar-menu')
span_elemets = menu_element.find_elements(By.TAG_NAME,'span')
span_elemets[0].click()

# 点击添加客户按钮
webDriver.find_element(By.CLASS_NAME,'add-one-area').click()

# 缓存1s
time.sleep(1)

# 添加客户信息
col_elemet = webDriver.find_element(By.CLASS_NAME,'add-one-area')
col_elemet.find_element(By.CLASS_NAME,'btn-md').click()
form_controls = col_elemet.find_elements(By.CLASS_NAME,'form-control')
form_controls[0].send_keys('罗湖人民医院')
form_controls[1].send_keys('0755-120')
form_controls[2].send_keys('深圳市罗湖区友谊路人民医院')

# 点击创建按钮
item_elements = col_elemet.find_element(By.CLASS_NAME,'btn-xs').click()

# 缓存1s
time.sleep(1)

# 获取添加的客户信息
result_element = webDriver.find_element(By.CLASS_NAME,'search-result-item')
result_element_itemrs = result_element.find_elements(By.CLASS_NAME,'search-result-item-field')

# 存储客户信息相关的列表
result_element_itemrs_list = []
for e in result_element_itemrs:
	for e in e.find_elements(By.TAG_NAME, 'span'):
		result_element_itemrs_list.append(e.text)
print(result_element_itemrs_list)


# 校验：检查输入的客户信息
expected =  [
	'客户名：',
	'罗湖人民医院',
	'联系电话：',
	'0755-120',
	'地址：',
	'深圳市罗湖区友谊路人民医院'
]
if result_element_itemrs_list == expected:
	print('测试通过')
else:
	print('测试不通过')

webDriver.quit()