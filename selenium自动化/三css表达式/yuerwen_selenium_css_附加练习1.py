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
from selenium.webdriver.common.by import By
import time

# 创建Chrome的驱动器
wd = webdriver.Chrome()

# 创建等待时间
wd.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://www.51job.com'
wd.get(web_file)

# 输入python关键字
wd.find_element(By.CSS_SELECTOR,'#kwdselectid').send_keys('测试开发')
wd.find_element(By.CSS_SELECTOR,'#work_position_click > .dicon').click()
category_hz_element = wd.find_element(By.CSS_SELECTOR,
                                      '#work_position_click_center_right_list_000000  '
                                      '#work_position_click_center_right_list_category_000000_040000')
# category_hz_element.clear()
category_hz_element.click()
# 点击确认按钮
wd.find_element(By.CSS_SELECTOR,'#work_position_click_bottom_save').click()
# 点击搜索按钮
wd.find_element(By.CSS_SELECTOR,'.radius_5 > .top_wrap button').click()

# 月薪范围：1.5-2w
wd.find_elements(By.CSS_SELECTOR,'.j_filter .fbox > .fmt > .clist a')[9].click()

time.sleep(1)

# 获取职位和公司
# joblist_element = wd.find_element(By.CSS_SELECTOR,'.j_joblist')
for e in wd.find_elements(By.CSS_SELECTOR,'.j_joblist .e'):
	job_name = e.find_element(By.CSS_SELECTOR,'.el > .t span[title]').get_attribute('title')
	job_time = e.find_element(By.CSS_SELECTOR, '.el > .t .time').text
	job_sal = e.find_element(By.CSS_SELECTOR, '.el > .info .sal').text
	blank = e.find_element(By.CSS_SELECTOR, '.er > a[target]').get_attribute('title')
	print(f'{job_name} | {job_time} | {job_sal} | {blank}')
	
# 关闭web网页
wd.quit()