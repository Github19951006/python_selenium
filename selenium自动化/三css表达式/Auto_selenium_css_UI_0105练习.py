"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2021/11/19
@File   :Auto_selenium_css_UI_0105练习.py
"""
'''
UI-0105

测试步骤：
1. 使用正确的管理员账号、密码登录白月SMS系统
2. 点击添加药品，输入正确格式的 药品名、编号和 描述
点击创建

预期结果：
1 登录成功
2. 检查药品列表第一项结果中 药品名、编号和 描述  都是正确的


'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建webdriver驱动器
webDriver = webdriver.Chrome()

# 设置等等时间
webDriver.implicitly_wait(5)

# 获取打开自动化网页
webDriver.get(r'http://127.0.0.1/mgr/sign.html')

# 登录
# 根据ID选择元素，返回的就是该元素对应的webdriver对象
element = webDriver.find_element(By.ID, 'username').send_keys('byhy')
element = webDriver.find_element(By.ID,'password').send_keys('88888888')
webDriver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

# 缓存1s
time.sleep(1)

# 获取左侧菜单，点击药品按钮
webDriver.find_element(By.CSS_SELECTOR,'.sidebar-menu li:nth-of-type(3) span').click()

# 点击添加药品按钮
webDriver.find_element(By.CSS_SELECTOR,'.add-one-area [type="button"]').click()

# 添加药品信息
div_elemets = webDriver.find_elements(By.CSS_SELECTOR,'.add-one-area '
                                                      '.col-sm-8 div [class="form-control"]')
div_elemets[0].send_keys('儿童益生菌饮料')
div_elemets[1].send_keys('10001010')
div_elemets[2].send_keys('促进小孩消化吸收，健全脾胃')

# 点击创建按钮
webDriver.find_element(By.CSS_SELECTOR,'.add-one-area .col-sm-12 [type="button"]').click()

# 缓存1s
time.sleep(1)

# 获取添加的药品信息
item = webDriver.find_element(By.CSS_SELECTOR,'.container-fluid .search-result-item')
result_element_itemrs = item.find_elements(By.CSS_SELECTOR,'.search-result-item-field')

# 存储药品信息相关的列表
result_element_itemrs_list = []
def result_itemrs():
	for e in result_element_itemrs:
		for e in e.find_elements(By.TAG_NAME, 'span'):
			result_element_itemrs_list.append(e.text)
	print(result_element_itemrs_list)
result_itemrs()


# 校验：检查输入的药品信息
expected =  [
	'药品：',
	'儿童益生菌饮料',
	'编号：',
	'10001010',
	'描述：',
	'促进小孩消化吸收，健全脾胃'
]

if result_element_itemrs_list == expected:
	print('----->测试通过')
else:
	print('----->测试不通过')

# 关闭浏览器
webDriver.quit()