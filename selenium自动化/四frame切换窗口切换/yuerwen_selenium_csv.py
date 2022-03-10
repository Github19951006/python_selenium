"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :yuerwen_selenium_css_2.py
"""
import csv

'''
登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词： python
    地区选择 ：上海
    职能类别选： 计算机/互联网/通信/电子 -> 测试 -> 所有
    公司性质选： 上市公司
    工作年限选：  1-3 年
    
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
 
    Python开发工程师 | 上海纳帕科技有限公司 | 上海 | 1.2-1.6万/月 | 04-27
    Python高级开发工程师 | 上海直真节点有限公司 | 上海 | 1.5-2万/月 | 04-27
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 打开Chrome浏览器驱动
chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
web_driver = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
web_driver.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://www.51job.com'
web_driver.get(web_file)

# 点击高级搜索
web_driver.find_element(By.CSS_SELECTOR,'.Fm .more').click()

# 输入选择关键词
web_driver.find_element(By.ID,'kwdselectid').send_keys('python')

# 工作地点选择
web_driver.find_element(By.CSS_SELECTOR,'#work_position_input').click()

# 确保界面稳定
time.sleep(1)

# 取消 已经选择的
web_driver.implicitly_wait(1) # implicitly_wait(1) 隐式等待
selectedCityEles = web_driver.find_elements(By.CSS_SELECTOR,'#work_position_click_center_right_list_000000 em[class=on]')
web_driver.implicitly_wait(1)
# 点击取消已经选择了的地方
for e in selectedCityEles:
	e.click()
	
# 选深圳
web_driver.find_element(By.CSS_SELECTOR,'#work_position_click_center_right_list_category_000000_040000').click()
# 点击确认 保存选择
web_driver.find_element(By.CSS_SELECTOR,'#work_position_click_bottom_save').click()


# 职能类别选： 计算机/互联网/通信/电子 -> 测试 -> 所有
# 这个里会出现覆盖ui的问题
'''
原因：UI覆盖了元素定位
解决办法：
web_driver.execute_script('arguments[0].click()',element对象)
'''
funtype_click = web_driver.find_element(By.CSS_SELECTOR,'#funtype_click')
web_driver.execute_script('arguments[0].click()',funtype_click)
web_driver.find_element(By.CSS_SELECTOR,'#funtype_click_center_right_list_category_0100_2700').click()
web_driver.find_element(By.CSS_SELECTOR,'#funtype_click_center_right_list_sub_category_each_0100_2700').click()
# 点击确认按钮
web_driver.find_element(By.CSS_SELECTOR,'#funtype_click_bottom_save').click()

# 公司性质选 上市公司
web_driver.find_element(By.ID,'cottype_list').click()
web_driver.find_element(By.CSS_SELECTOR,'#cottype_list span.li[data-value="10"]').click()

# 工作年限
web_driver.find_element(By.ID,'workyear_list').click()
web_driver.find_element(By.CSS_SELECTOR,'#workyear_list span.li[data-value="02"]').click()

# 点击搜索
web_driver.find_element(By.CSS_SELECTOR,'.p_but').click()


# joblist_element = web_driver.find_element(By.CSS_SELECTOR,'.j_joblist')
# for e in joblist_element.find_elements(By.CSS_SELECTOR,'.e'):
# 	job_name = e.find_element(By.CSS_SELECTOR,'.el > .t span[title]').get_attribute('title')
# 	job_time = e.find_element(By.CSS_SELECTOR, '.el > .t .time').text
# 	job_sal = e.find_element(By.CSS_SELECTOR, '.el > .info .sal').text
# 	blank = e.find_element(By.CSS_SELECTOR, '.er > a[target]').get_attribute('title')
# 	at = e.find_element(By.CSS_SELECTOR,'.el > .info .at').text[:2]
	# print(f'{job_name} | {blank} | {at} | {job_sal} | {job_time[:-2]}')

# 存储初始化数据
yuer_list = []
# 搜索结果分析（优化）
jobs = web_driver.find_elements(By.CSS_SELECTOR,'.j_joblist .e')

# 当前窗口的句柄
main_handl = web_driver.current_window_handle

def yuer():
	# 进入详情页
	joblist_elements = web_driver.find_elements(By.CSS_SELECTOR, '.j_joblist .e')
	jobs_ms = []
	for job in joblist_elements[:2]:
		job.click()
		
		for handle in web_driver.window_handles:
			# 先切换到该窗口
			web_driver.switch_to.window(handle)
		
		job_msgs = web_driver.find_elements(By.CSS_SELECTOR, '.tCompany_main  .tBorderTop_box  .job_msg  p')
		for job in job_msgs:
			a = ''.join(job.text.split())
			jobs_ms.append(a)
			strField.extend(jobs_ms)
		web_driver.switch_to.window(main_handl)
		time.sleep(5)
	
	with open('csvData.csv', 'w', newline='', encoding='utf-8') as f:  # 创建csv文件
		csv_file = csv.writer(f)
		csv_file.writerow(["职位", '发布日期', '工资', '公司', '职位描述'])  # 写入列的名称
		for i in yuer_list:
			csv_file.writerow(i)


for job in jobs:
	filelds = job.find_elements(By.CSS_SELECTOR,'.jname, .cname, .time, .sal')
	strField = [fileld.text for fileld in filelds]
	yuer()
	time.sleep(3)
	yuer_list.append(strField)

print(yuer_list)



# 关闭web网页
web_driver.quit()