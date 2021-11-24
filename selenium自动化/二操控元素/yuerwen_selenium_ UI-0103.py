"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_ UI-0102.py
"""
'''
测试步骤：
1. 使用正确的管理员账号、密码登录白月SMS系统
2. 点击添加客户，
	2.1输入客户名为 南京中医院 的客户
	2.2输入客户联系电话
	2.3输入地址
	2.4点击创建
预期结果：
1 登录成功
2. 检查客户列表第一项结果中客户名、电话、地址信息都是正确的
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


web_file = Service(r'd:\webdrivers\chromedriver.exe')
webdriver_object = webdriver.Chrome(service=web_file)
# 设置等待时间
webdriver_object.implicitly_wait(5)
# 通过get方法  打开web网页
webdriver_object.get(r'http://127.0.0.1/mgr/sign.html')

# 根据ID选择元素，返回的就是该元素对应的webdriver对象
webdriver_object.find_element(By.ID, 'username').send_keys('byhy')
# 输入文本
# element.send_keys('byhy')
webdriver_object.find_element(By.ID,'password').send_keys('88888888')
# 点击
webdriver_object.find_element(By.CLASS_NAME,'btn-primary').click()

# 获取的是第一个element对象
search_result_item_element = webdriver_object.find_element(By.CLASS_NAME,'search-result-item')
search_result_item_element.find_element(By.CLASS_NAME,'btn-xs').click()

input_element = search_result_item_element.find_elements(By.CLASS_NAME,'form-control')
input_element[0].clear()
input_element[0].send_keys('南京省中医院')

# 获取文本框的信息，存储到列表中
input_value = [input_element[i].get_attribute('value') for i in range(3)]
search_result_item_element.find_element(By.CLASS_NAME,'btn-xs').click()

time.sleep(0.1)

search_result_item_fields_elements = search_result_item_element\
	.find_elements(By.CLASS_NAME,'search-result-item-field')
list_element = [e.text.split('：')[1] for e in search_result_item_fields_elements]
print(list_element)
if list_element == input_value:
	print('测试通过')
else:
	print('测试不通过')
	
webdriver_object.quit()


