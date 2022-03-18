"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/24
@File   :Auto_selenium_css_下_附加练习1.py
"""
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
from selenium.webdriver.common.by import By
import time

# 创建Chrome的驱动器
webDriver = webdriver.Chrome()

# 创建等待时间
webDriver.implicitly_wait(5)

# 调用webdriver对象的 get方法，让浏览器打开指定网址
web_file = r'http://www.51job.com'
webDriver.get(web_file)

# 点击高级搜索
webDriver.find_element(By.CSS_SELECTOR,'.more').click()

# 输入python关键字
webDriver.find_element(By.CSS_SELECTOR,'.d_lt #kwdselectid').send_keys('测试开发')
# 工作地点选择
webDriver.find_element(By.CSS_SELECTOR,'#work_position_input').click()

# 确保界面稳定(有页面交互，所以要设置一下缓冲时间)
time.sleep(1)

# 取消 已经选择的工作地点
selectedCityEles = webDriver.find_elements(By.CSS_SELECTOR,
                                            '#work_position_click_center_right_list_000000 em[class=on]')
webDriver.implicitly_wait(5)
# 点击取消已经选择了的地方
for e in selectedCityEles:
	e.click()

# 重新选择深圳
webDriver.find_element(By.CSS_SELECTOR,
                       '#work_position_click_center_right_list_category_000000_040000').click()
# 点击确定按钮
webDriver.find_element(By.CSS_SELECTOR,
                       '#work_position_click_bottom_save').click()

# 职能类别选： 计算机/互联网/通信/电子 -> 测试 -> 所有
# 这个里会出现覆盖ui的问题
webDriver.find_element(By.CSS_SELECTOR,
                '.d_lt #funtype_click').click()

webDriver.find_element(By.CSS_SELECTOR,
                '#funtype_click_center_right_list_category_0100_2700').click()
webDriver.find_element(By.CSS_SELECTOR,
                '#funtype_click_center_right_list_sub_category_each_0100_2700').click()
# 点击确认按钮
webDriver.find_element(By.CSS_SELECTOR,
                '#funtype_click_bottom_save').click()

# 公司性质选 上市公司
webDriver.find_element(By.CSS_SELECTOR,'#cottype_list').click()
webDriver.find_element(By.CSS_SELECTOR,'#cottype_list .ul [title="上市公司"]').click()

# 工作年限
webDriver.find_element(By.CSS_SELECTOR,'#workyear_list').click()
webDriver.find_element(By.CSS_SELECTOR,'#workyear_list .ul [title="1-3年"]').click()
webDriver.find_element(By.CSS_SELECTOR,'.p_sou .p_but').click()

time.sleep(1)

# 获取职位和公司
'''
for e in webDriver.find_elements(By.CSS_SELECTOR,'.j_joblist .e'):
	job_name = e.find_element(By.CSS_SELECTOR,'.el > .t span[title]').get_attribute('title')
	job_time = e.find_element(By.CSS_SELECTOR, '.el > .t .time').text
	job_sal = e.find_element(By.CSS_SELECTOR, '.el > .info .sal').text
	blank = e.find_element(By.CSS_SELECTOR, '.er > a[target]').get_attribute('title')
	print(f'{job_name} | {job_time} | {job_sal} | {blank}')
'''

# 搜索结果分析（优化）
jobs = webDriver.find_elements(By.CSS_SELECTOR,'.j_joblist .e')
for job in jobs:
	filelds = job.find_elements(By.CSS_SELECTOR,'.jname, .cname, .time, .sal')
	strField = [fileld.text for fileld in filelds]
	print(' | '.join(strField))
	
# 关闭web网页
webDriver.quit()