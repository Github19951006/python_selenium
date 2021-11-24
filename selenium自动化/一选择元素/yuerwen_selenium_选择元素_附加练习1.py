"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_选择元素_附加练习1.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')

# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
webdriver_obj = webdriver.Chrome(service=webdriver_file)

# 设置等等时间
webdriver_obj.implicitly_wait(5)

# 根据webdriver对象的get方法 打开指定的web地址
web_file = r'http://cdn1.python3.vip/files/selenium/jsweather.html'
webdriver_obj.get(web_file)

webelement = webdriver_obj.find_element(By.ID,'forecastID')
dl_element = webelement.find_elements(By.TAG_NAME,'dl')

# citys_level_list 存放城市和最低温度的信息
citys_level_list = []
for element in dl_element:
	name = element.find_element(By.TAG_NAME, 'dt').text
	ltemp = element.find_element(By.TAG_NAME, 'span').text
	# print(f'{name}:{ltemp}')
	
	ltemp = int(ltemp.replace('℃',''))
	citys_level_list.append([name,ltemp])
print(citys_level_list)

# 算法
lowest = None
lowestCitys = []  # 温度最低城市列表
for one in citys_level_list:
    curcity = one[0]
    ltemp = one[1]
    # 发现气温更低的城市
    if lowest == None or ltemp < lowest:
        lowest = ltemp
        lowestCitys = [curcity]
    #  温度和当前最低相同，加入列表
    elif ltemp == lowest:
        lowestCitys.append(curcity)
	    
print(f"温度最低为:{lowest}℃, 城市有:{' '.join(lowestCitys)}")
webdriver_obj.quit()