"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2022/01/04
@File   :test.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
driver.implicitly_wait(5)

mobile_emulation = { "deviceName": "Nexus 5" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())

driver.get(r'http://cdn1.python3.vip/files/selenium/test4.html')

input('')
driver.quit()


