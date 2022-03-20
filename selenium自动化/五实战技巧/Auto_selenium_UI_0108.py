"""
@Project ：python_selenium 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/19
@File   :Auto_selenium_frame_1.py
"""

'''
UI-0107
测试步骤：
1. 使用正确的管理员账号、密码登录白月SMS系统
2. 在系统中添加3种药品，依次为
'青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装'
'青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装'
'青霉素盒装3','YP-32342343','青霉素注射液，每支15ml，40支装'

在系统中添加3个客户，依次为
'南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501'
'南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502'
'南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503'

进入订单管理界面，添加一个订单，
客户选择 南京中医院2
药品选择 青霉素盒装1
数量填入 100盒

预期结果
1 登录成功
2. 添加订单成功
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 创建Chrome 驱动器
webDriver = webdriver.Chrome()
# 设置等等时间
webDriver.implicitly_wait(5)
# 打开网页地址
webDriver.get(r'http://127.0.0.1/mgr/sign.html')

# 登录
# 根据ID选择元素，返回的就是该元素对应的webdriver对象
element = webDriver.find_element(
	By.ID, 'username'
).send_keys('byhy')
element = webDriver.find_element(
	By.ID,'password'
).send_keys('88888888')
webDriver.find_element(
	By.CSS_SELECTOR,'button[type=submit]'
).click()

# 缓存1s
time.sleep(1)

# 获取左侧菜单，点击药品按钮
webDriver.find_element(
	By.CSS_SELECTOR,'.sidebar-menu li:nth-of-type(3) span'
).click()

elements = webDriver.find_elements(By.CSS_SELECTOR,'.container-fluid .search-result-item')
for e in elements:
	e.find_elements(By.CSS_SELECTOR,'label')[1].click()
	# 打印 弹出框 提示信息
	print(webDriver.switch_to.alert.text)
	time.sleep(1)
	# 点击 OK 按钮
	webDriver.switch_to.alert.accept()

# # 点击添加药品按钮
# webDriver.find_element(
# 	By.CSS_SELECTOR,'.add-one-area [type="button"]'
# ).click()
#
# # 添加药品信息
# div_elemets = webDriver.find_elements(
# 	By.CSS_SELECTOR,'.add-one-area .col-sm-8 div [class="form-control"]'
# )
# i = 0
# while i < 3:
# 	div_elemets[0].send_keys(f'青霉素盒装{i+1}')
# 	div_elemets[1].send_keys(f'YP-32342341{i+1}')
# 	div_elemets[2].send_keys(f'青霉素注射液，每支15ml，{(i+2)*10}支装')
# 	i = i+1
# 	# 点击创建按钮
# 	webDriver.find_element(
# 		By.CSS_SELECTOR,'.add-one-area .col-sm-12 [type="button"]'
# 	).click()

# # 缓存1s
# time.sleep(1)
#
# # 获取左侧菜单，点击客户按钮
# webDriver.find_elements(
# 	By.CSS_SELECTOR,'.sidebar-menu span'
# )[0].click()
#
#
# # 点击添加客户按钮
# webDriver.find_element(
# 	By.CSS_SELECTOR,'.add-one-area [type="button"]'
# ).click()
#
# # 添加客户信息
# col_elemet = webDriver.find_element(By.CLASS_NAME, 'add-one-area')
# col_elemet.find_element(By.CLASS_NAME, 'btn-md').click()
# form_controls = col_elemet.find_elements(By.CLASS_NAME, 'form-control')
# f = 0
# while f < 3:
# 	form_controls[0].send_keys(f'罗湖人民医院{f+1}')
# 	form_controls[1].send_keys(f'255186785{f+1}')
# 	form_controls[2].send_keys(f'深圳市-罗湖区-友谊路-人民医院--50{f+1}')
# 	f = f + 1
#
# 	# 点击创建按钮
# 	col_elemet.find_element(By.CLASS_NAME,'btn-xs').click()
#
# # 获取左侧菜单，点击订单按钮
# webDriver.find_elements(
# 	By.CSS_SELECTOR,'.sidebar-menu span'
# )[2].click()
# # 添加客户
# webDriver.find_element(By.CSS_SELECTOR,'.add-one-area .btn').click()
#
# # 输入订单名称
# webDriver.find_element(
# 	By.CSS_SELECTOR,'.add-one-area  .form-control'
# ).send_keys('Auto-yuerwen-test1')
#
# # 获取两个select 对象
# select_elements = webDriver.find_elements(By.CSS_SELECTOR,'.add-one-area select')
# # 选择客户
# Select(select_elements[0]).select_by_visible_text("罗湖人民医院2")
# # 选择药品
# Select(select_elements[1]).select_by_visible_text("青霉素盒装1")
#
# webDriver.find_element(
# 	By.CSS_SELECTOR,'input[type = "number"]'
# ).send_keys('100')
# webDriver.find_element(
# 	By.CSS_SELECTOR,'.add-one-area .btn-xs'
# ).click()
#
# # 获取药品订单信息，存储到 search_result_item_list 列表中
# spans = webDriver.find_elements(
# 	By.CSS_SELECTOR,'.content-wrapper .container-fluid '
# 	                '.search-result-item span'
# )
# p_element = webDriver.find_element(
# 	By.CSS_SELECTOR,'.content-wrapper .container-fluid '
# 	                '.search-result-item p'
# )
# # 获取订单的信息
# search_result_item_list = [e.text for e in spans[:2]]
# for e in spans[4:7]:
# 	search_result_item_list.append(e.text)
# # 获取p标签的 青霉素信息和个数
# search_result_item_list.append(p_element.text)
# print(search_result_item_list)
# expect = [
# 	'订单：',
# 	'Auto-yuerwen-test1',
# 	'客户：',
# 	'罗湖人民医院2',
# 	'药品：',
# 	'青霉素盒装1 * 100'
# ]
#
# # 判断是否符合预期
# if search_result_item_list == expect:
# 	print('---> 测试通过')
# else:
# 	print('---> 测试不通过')

# 关闭浏览器
webDriver.quit()