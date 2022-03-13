"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/09
@File   :Auto_selenium_className.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建webDriver 实例对象
webDriver = webdriver.Chrome()

# 设置等等时间
webDriver.implicitly_wait(5)

# 指定打开的网址
webDriver.get(r'http://cdn1.python3.vip/files/selenium/jsweather.html')

# 通过ID选择器  tag_name 选择器
forecast_element = webDriver.find_element(By.ID,'forecastID')
dl_element = forecast_element.find_elements(By.TAG_NAME,'dl')

# 创建一个列表 存储【城市+温度】
city_number_list = []

for element in dl_element:
	city_name = element.find_element(By.TAG_NAME,'dt').text
	number = element.find_element(By.TAG_NAME,'span').text
	number_end = int(number.replace('℃',''))
	city_number_list.append([city_name,number_end])
print(city_number_list)

# 算法
'''
lowest_citys：最低温度城市
lowes_number：最低温度值
city：城市
lowes：温度值
'''
lowes_number = None
lowest_citys = []
for elemnt in city_number_list:
	city = elemnt[0]
	lowes = elemnt[1]
	if lowes_number == None or lowes < lowes_number:
		lowes_number = lowes
		lowest_citys = [city]
	elif lowes_number == lowes:
		lowest_citys.append(city)
print(lowest_citys)
print(f"温度最低为:{lowes_number}℃, 城市有:{' |<|>| '.join(lowest_citys)}")
# 关闭浏览器
webDriver.quit()



