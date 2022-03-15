"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/15
@File   :Auto_selenium_css_选择子元素.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
css 选择器支持通过任何属性来选择元素，语法是用一个方括号 []

'''

webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(2)

# 打开web路径
web_file = r'http://cdn1.python3.vip/files/selenium/sample1.html'
webDriver.get(web_file)

# 还可以选择 属性值 包含 某个字符串 的元素  *  语法：'a[href *= "miitbeian"]'
# her_element = webDriver.find_element(By.CSS_SELECTOR,'[href="http://www.miitbeian.gov.cn"]')
her_element = webDriver.find_element(By.CSS_SELECTOR,'a[href *= "miitbeian"]')

# 获取元素属性值
print(her_element.get_attribute('href'))
# 获取元素文本
print(her_element.text)

webDriver.quit()