"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_选择元素UI_001练习.py
"""
# 完成用例 UI-0101 的自动化
'''
测试步骤：
1. 使用正确的管理员账号、密码登录白月SMS系统
2. 检查左侧菜单

预期结果
1. 前三项菜单名称分别为：
客户
药品
订单
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')

# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
webdriver_obj = webdriver.Chrome(service=webdriver_file)

# 设置等等时间
webdriver_obj.implicitly_wait(5)

# 根据webdriver对象的get方法 打开指定的web地址
web_file = r'http://127.0.0.1/mgr/sign.html'
webdriver_obj.get(web_file)

# 输入信息
webdriver_obj.find_element(By.ID,'username').send_keys('byhy')
webdriver_obj.find_element(By.ID,'password').send_keys('88888888')
# 点击按钮
webdriver_obj.find_element(By.CLASS_NAME,'btn-primary').click()

element_obj = webdriver_obj.find_element(By.CLASS_NAME,'sidebar-menu')
span_obj_list = element_obj.find_elements(By.TAG_NAME,'span')

# 存储菜单栏的text
# element_list = []
# for span in span_obj_list:
# 	print(span.text)
# 	element_list.append(span.text)

# 优化代码list
# 列表推导式用法：[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]
element_list = [span.text for span in span_obj_list]
print(element_list)

# 校验：检查菜单
if element_list[:3] == ['客户','药品','订单']:
	print('测试通过')
else:
	print('测试不通过')

webdriver_obj.quit()
