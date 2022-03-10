"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_1.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://127.0.0.1/mgr/sign.html'
wd.get(web_file)

# 登录页面
# - input_username ：输入用户名
# - input_password ：输入密码
# - click_ ：点击按钮
input_username = wd.find_element(By.CSS_SELECTOR,'.form-group > #username').send_keys('byhy')
input_password = wd.find_element(By.CSS_SELECTOR,'.form-group > #password').send_keys('88888888')
click_ = wd.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

# 操作子页面,添加客户详细信息
# - 点击添加客户
wd.find_element(By.CSS_SELECTOR,'.container-fluid .btn-md').click()
elements = wd.find_elements(By.CSS_SELECTOR,'.add-one-area .form-control')
elements[0].send_keys('南京中医院') # 输入客户名
elements[1].send_keys('1101191190') # 输入联系电话
wd.find_element(By.CSS_SELECTOR,'.add-one-area textarea').send_keys('东莞理工学院') # 输入地址
wd.find_element(By.CSS_SELECTOR,'.add-one-area [type="button"].btn-xs').click()

# 设置缓存时间0.1S
time.sleep(0.1)

# 修改客户名为 南京省中医院
# - 点击编辑
wd.find_element(By.CSS_SELECTOR,'.search-result-item > .search-result-item-actionbar > .btn-group > label').click()
# - 修改客户名称
result_name = wd.find_element(By.CSS_SELECTOR,'.search-result-item ' '.form-control')
result_name.clear()
result_name.send_keys('南京省中医院1')

# - 点击确定
wd.find_element(By.CSS_SELECTOR,'.search-result-item-actionbar > .btn-group > label').click()


# 判断用例是否通过
# 获取前面的6个text文本信息，存储到list中
if_elements = wd.find_elements(By.CSS_SELECTOR,'.container-fluid .search-result-item span')[:6]
texts = [e.text for e in if_elements]

# 预期结果
expecteds = ['客户名：', '南京省中医院1', '联系电话：', '1101191190', '地址：', '东莞理工学院']

print('\n**检查点** 客户信息和添加内容是否一致')
# 判断输入的信息和预期结果是否一致
if texts == expecteds:
	print('-----> 测试通过')
else:
	print('-----> 测试不通过')
	
# 关闭
wd.quit()