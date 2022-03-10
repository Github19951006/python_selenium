"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_1.py
"""
'''
登录 51job ，
http://www.51job.com

输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉），
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

Python高级开发工程师 | 03-23发布 | 1.5-2万/月 | 欧睿恒（大连）信息技术有限公司
Python开发工程师 | 03-23发布 | 3-4万/月 | 苏州格勤电子科技有限公司
Python爬虫工程师 | 03-23发布 | 0.8-1.5万/月 | 杭州筑龙信息技术股份有限公司
Python高级开发工程师 | 03-23发布 | 1.5-3万/月 | 杭州德适生物科技有限公司
Python开发工程师 | 03-23发布 | 1-1.3万/月 | 浙江大云物联科技有限公司
Python软件开发工程师 | 03-23发布 | 0.8-1万/月 | 上海特速网络科技有限公司
Python开发工程师 | 03-23发布 | 1.5-2万/月 | 上海豪亿信息科技有限公司
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://www.51job.com'
wd.get(web_file)

# 输入python关键字
wd.find_element(By.CSS_SELECTOR,'#kwdselectid').send_keys('python')
wd.find_element(By.CSS_SELECTOR,'#work_position_click > .dicon').click()
category_hz_element = wd.find_element(By.CSS_SELECTOR,'#work_position_click_center_right_list_000000  #work_position_click_center_right_list_category_000000_080200')
# category_hz_element.clear()
category_hz_element.click()
# 点击确认按钮
wd.find_element(By.CSS_SELECTOR,'#work_position_click_bottom_save').click()
# 点击搜索按钮
wd.find_element(By.CSS_SELECTOR,'.radius_5 > .top_wrap button').click()

# 当前窗口的句柄
main_handl = wd.current_window_handle

joblist_elements = wd.find_elements(By.CSS_SELECTOR,'.j_joblist .e')
jobs = []
for job in joblist_elements[:2]:
	job.click()
	for handle in wd.window_handles:
		# 先切换到该窗口                            
		wd.switch_to.window(handle)
  
	job_msgs = wd.find_elements(By.CSS_SELECTOR,'.tCompany_main  .tBorderTop_box  .job_msg  p')
	for job in job_msgs:
		a = ''.join(job.text.split())
		jobs.append(job.text)
		
	print('===========================-----------------------------==========================')
	wd.switch_to.window(main_handl)
print(jobs)
csvFile = open("csvData.csv", "w")            #创建csv文件
writer = csv.writer(csvFile)                  #创建写的对象
#先写入columns_name
writer.writerow(["职位描述信息"])     #写入列的名称
writer.writerow(jobs)
print('')


# 关闭web网页
# wd.quit()