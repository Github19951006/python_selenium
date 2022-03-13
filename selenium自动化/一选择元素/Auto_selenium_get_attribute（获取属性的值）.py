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

elemet = webDriver.find_element(By.ID,'suggestion')

# get_attribute 获取属性的值
'''
<input type="text" id="suggestion" placeholder="一句话建议" style="height: 1.2rem;">
'''
text = elemet.get_attribute('placeholder') # 一句话建议
print(text)

print('==================outerHTML========innerHTML===================================')
'''
outerHTML整个元素对应 的HTML文本内容:
<div class="result-item" id="1">
          <p class="name">包钢股份</p>
          <p>代码：<span>600010</span></p>
        </div>
        
innerHTML内部 的HTML文本内容:

          <p class="name">包钢股份</p>
          <p>代码：<span>600010</span></p>
'''
# 返回页面 ID为1 的元素
element_id = webDriver.find_element(By.ID,'1')
print(f'outerHTML整个元素对应 的HTML文本内容:\n{element_id.get_attribute("outerHTML")}')
print(f'innerHTML内部 的HTML文本内容:\n{element_id.get_attribute("innerHTML")}')

# 获取输入框中的文本 get_attribute('value')
element_input = webDriver.find_element(By.ID,'kw')
ret = input('输入信息：')
element_input.send_keys(f'{ret}')
print(element_input.get_attribute('value'))

# 关闭浏览器
webDriver.quit()


