"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2022/01/07
@File   :yuerwen_xpath_1.py
"""
# 根据属性来选择
# 语法：[@属性名 = ‘属性值’]
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 打开指定网页地址
web_files = r'http://cdn1.python3.vip/files/selenium/test1.html'
wd.get(web_files)

# -- 根据id属性选择选择   //*[@id='west']
# element = wd.find_element(By.XPATH,"//*[@id='west']")
# print(element.get_attribute('outerHTML'))

# -- 根据class属性选择  可以这样 //select[@class='single_choice']
# element = wd.find_element(By.XPATH,"//select[@class='single_choice']")
# print(element.get_attribute('outerHTML'))

# -- 根据其他属性  //*[@multiple]
# element = wd.find_element(By.XPATH,"//*[@multiple]")
# print(element.get_attribute('outerHTML'))

# -- 属性值包含字符串
# 要选择 style属性值 包含 color 字符串的 页面元素 ，可以这样 //*[contains(@style,'color')]
# -- 属性包含字符串 contains(@属性名,'要包含的属性名')函数
element_contains = wd.find_element(By.XPATH,"//*[contains(@style,'color')]")
print(element_contains.get_attribute('outerHTML'))

# 要选择 style属性值 以 color 字符串 开头 的 页面元素 , 可以这样 //*[starts-with(@style,'color')]
# -- 属性以指定字符串开头  starts-with(@属性名,'指定的属性名')
element_starts_with = wd.find_element(By.XPATH,"//*[starts-with(@style,'color')]")
print(element_starts_with.get_attribute('outerHTML'))



# element_starts_end = wd.find_element(By.XPATH,"//*[end-with(@style,'color')]")
# print(element_starts_end.get_attribute('outerHTML'))
wd.quit()