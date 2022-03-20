"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/01/07
@File   :Auto_xpath_1.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个Chrome驱动器
wd = webdriver.Chrome()
# 创建等待时间
wd.implicitly_wait(5)

# 打开指定网页地址
web_files = r'http://cdn1.python3.vip/files/selenium/test1.html'
wd.get(web_files)

# 绝对路径选择：xpath 语法中，整个HTML文档根节点用'/‘表示，
# 注意 / 有点像 CSS中的 > , 表示直接子节点关系。
element_xpath = wd.find_element(By.XPATH,'/html/body/div')
print(element_xpath.get_attribute('innerHTML'))

print('---------------------')

# 相对路径选择: xpath需要前面加 // , 表示从当前节点往下寻找所有的后代元素,不管它在什么位置。
element_xpath = wd.find_element(By.XPATH,'//select')
print(element_xpath.get_attribute('outerHTML'))

# 通配符
print('---------------------')
elements = wd.find_elements(By.XPATH, "//select/*")
for element in elements:
    print(element.get_attribute('outerHTML'))
    
wd.quit()