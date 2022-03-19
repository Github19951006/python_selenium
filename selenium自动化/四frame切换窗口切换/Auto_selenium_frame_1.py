"""
@Project ：python_selenium 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/19
@File   :Auto_selenium_frame_1.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(5)

# 打开浏览器
webDriver.get(r'https://cdn2.byhy.net/files/selenium/sample2.html')

# 先根据id属性值 'frame1'，切换到iframe中frame1
webDriver.switch_to.frame('frame1')

# 使用组选择器
# 获取plant、animal
plant_annimal_elements = webDriver.find_elements(By.CSS_SELECTOR,'.plant, .animal')
for element in plant_annimal_elements:
	print(element.text)

webDriver.quit()