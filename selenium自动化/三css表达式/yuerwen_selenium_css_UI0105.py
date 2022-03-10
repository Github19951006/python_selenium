"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_UI0105.py
"""
'''
UI0105的用例:
操作步骤：
1. 使用正确的管理员账号、密码登录白月SMS系统
2. 点击添加药品，输入正确格式的 药品名、编号和 描述
3. 点击创建
预期：
1 登录成功
2. 检查药品列表第一项结果中 药品名、编号和 描述  都是正确的
'''
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

# 获取左侧菜单，点击药品菜单
wd.find_element(By.CSS_SELECTOR,'.sidebar-menu li:nth-last-of-type(3) span').click()

# 操作子页面,添加药品详细信息
# - 点击添加药品按钮
wd.find_element(By.CSS_SELECTOR,'.add-one-area button').click()

# 获取添加药品的详细详细
elements = wd.find_elements(By.CSS_SELECTOR,'.add-one-area .col-sm-8 .form-control:nth-of-type(1)')
# - 药品名称
elements[0].send_keys('阿莫西林软膏')
# - 编号
elements[1].send_keys('0001')
# - 描述
elements[2].send_keys('中国好药膏')
# - 点击确定
wd.find_element(By.CSS_SELECTOR,'.add-one-area .btn-xs').click()

# 设置缓存时间
time.sleep(0.1)

# 判断用例是否通过
# 获取前面的6个text文本信息，存储到list中
if_elements = wd.find_elements(By.CSS_SELECTOR,'.container-fluid .search-result-item span')[:6]
texts = [e.text for e in if_elements]

# 预期结果
expecteds = ['药品：', '阿莫西林软膏', '编号：', '0001', '描述：', '中国好药膏']

print('\n**检查点** 药品信息和添加内容是否一致')
if texts == expecteds:
	print('-----> 测试通过')
else:
	print('-----> 测试不通过')
	
# 关闭浏览器
wd.quit()