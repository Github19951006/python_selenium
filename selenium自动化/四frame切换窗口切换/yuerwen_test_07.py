"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/23
@File   :yuerwen_test_07.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# 导入Select类
from selenium.webdriver.support.ui import Select

chromedriver_files = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_files)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_files = r'http://127.0.0.1/mgr/sign.html'
wd.get(web_files)

# 输入信息
wd.find_element(By.ID,'username').send_keys('byhy')
wd.find_element(By.ID,'password').send_keys('88888888')
# 点击按钮
wd.find_element(By.CLASS_NAME,'btn-primary').click()

# 操作子页面,添加客户详细信息
# - 点击添加客户
for number_customer in range(3):
	wd.find_element(By.CSS_SELECTOR,'.container-fluid .btn-md').click()
	elements = wd.find_elements(By.CSS_SELECTOR,'.add-one-area .form-control')
	elements[0].send_keys(f'南京中医院{number_customer + 1}') # 输入客户名
	elements[1].send_keys(f'255186785{number_customer + 1}') # 输入联系电话
	wd.find_element(By.CSS_SELECTOR,'.add-one-area textarea').send_keys(f"江苏省-南京市-秦淮区-汉中路-50{number_customer + 1}") # 输入地址
	wd.find_element(By.CSS_SELECTOR,'.add-one-area [type="button"].btn-xs').click()
	time.sleep(2)

# 判断用例是否通过
# 获取前面的6个text文本信息，存储到list中
if_elements = wd.find_elements(By.CSS_SELECTOR,'.container-fluid .search-result-item span')[:6]
texts = [e.text for e in if_elements]

# 预期结果
expecteds = ['客户名：', '南京中医院3', '联系电话：', '2551867853', '地址：', '江苏省-南京市-秦淮区-汉中路-503']

print('\n**检查点** 客户信息和添加内容是否一致')
# 判断输入的信息和预期结果是否一致
if texts == expecteds:
	print('-----> 测试通过')
else:
	print('-----> 测试不通过')
	
# 设置缓存时间1S
time.sleep(1)
# 操作子页面,添加药品详细信息
# 获取左侧菜单，点击药品菜单
wd.find_element(By.CSS_SELECTOR,'.sidebar-menu li:nth-last-of-type(3) span').click()
# - 点击添加药品按钮
wd.find_element(By.CSS_SELECTOR,'.add-one-area button').click()

# - 获取添加药品的详细详细
elements = wd.find_elements(By.CSS_SELECTOR,'.add-one-area .col-sm-8 .form-control:nth-of-type(1)')
# 青霉素数量的初始值
number_quantity = 20
for number_drugs in range(3):
	# - 药品名称
	elements[0].send_keys(f'青霉素盒装{number_drugs + 1}')
	# - 编号
	elements[1].send_keys(f'YP-3234234{number_drugs + 1}')
	# - 描述
	elements[2].send_keys(f'青霉素注射液，每支15ml，{number_quantity + (number_drugs * 10)}支装')
	# - 点击确定
	wd.find_element(By.CSS_SELECTOR,'.add-one-area .btn-xs').click()
	time.sleep(2)
time.sleep(2)
if_elements = wd.find_elements(By.CSS_SELECTOR,'.container-fluid .search-result-item span')[:6]
texts = [e.text for e in if_elements]

# 预期结果
expecteds = ['药品：', '青霉素盒装3', '编号：', 'YP-32342343', '描述：', '青霉素注射液，每支15ml，40支装']
print('\n**检查点** 药品信息和添加内容是否一致')
if texts == expecteds:
	print('-----> 测试通过')
else:
	print('-----> 测试不通过')
	
# 操作子页面,添加订单管理
# 获取左侧菜单，点击订单
wd.find_element(By.CSS_SELECTOR,'.fa-paperclip').click()
# 点击添加订单
wd.find_element(By.CSS_SELECTOR,'.glyphicon-plus').click()
# 订单名称
wd.find_elements(By.CSS_SELECTOR,'.form-control')[0].send_keys('yuerwen_test_01')
# - 点击添加订单详细信息
elements = wd.find_elements(By.CSS_SELECTOR,'.xxx')
element1 = Select(elements[0])
element1.select_by_visible_text('南京中医院2')
element2 = Select(elements[1])
element2.select_by_visible_text('青霉素盒装1')
wd.find_element(By.CSS_SELECTOR,'.col-lg-8  input[type="number"]').send_keys('100')
wd.find_elements(By.CSS_SELECTOR,'.col-sm-12 .btn-xs')[0].click()

time.sleep(2)
if_elements = wd.find_elements(By.CSS_SELECTOR,'.search-result-item .search-result-item-field span')[:6]
texts = [e.text for e in if_elements]

# 预期结果
# 时间获取上有问题，所以测试不通过---后续再改
expecteds = ['订单：', 'yuerwen_test_01', '日期：', '2021-12-24 23:36:21', '客户：', '南京中医院2']
print('\n**检查点** 信息和添加内容是否一致')
if texts == expecteds:
	print('-----> 测试通过')
else:
	print('-----> 测试不通过')
# 关闭网页
# wd.quit()