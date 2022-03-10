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
# 指定打开的网址
webDriver.get(r'https://www.byhy.net/_files/stock1.html')

# 通过ID选择器  tag_name 选择器
elemet = webDriver.find_element(By.ID,'kw')
elemet.send_keys('通讯')
webDriver.find_element(By.ID,'go').click()

# time.sleep(1)

# 返回页面 ID为1 的元素
element_id = webDriver.find_element(By.ID,'1')
# 打印该元素的文字内容
print(element_id.text)

# 报错的原因：驱动点击之后，浏览器加载的时间比较慢，导致获取不到数据，报错没有定位到NoSuchElementException
# 解决办法：设置缓存时间
'''
selenium.common.exceptions.NoSuchElementException: Message:
no such element: Unable to locate element:
{"method":"css selector","selector":"[id="1"]"}
'''
# 关闭浏览器
webDriver.quit()


