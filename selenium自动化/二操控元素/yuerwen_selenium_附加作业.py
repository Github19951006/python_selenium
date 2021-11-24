"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/23
@File   :yuerwen_selenium_附加作业.py
"""
'''
打开qq音乐， https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27

找出其中排名下降的歌曲和演唱者
最终结果显示的结果如下：
孤独                ： G.E.M. 邓紫棋
Lovesick Girls     ： BLACKPINK
落幕人              ： 任然
幸存者              ： 林俊杰
刁钻                ： 任然
注意：界面有时会弹出广告框，可以先手动关闭掉，防止其影响自动化爬取信息
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

chromedriver_file = Service(r'd:\webdrivers\chromedriver.exe')
wd = webdriver.Chrome(service=chromedriver_file)

# 创建等待时间
wd.implicitly_wait(5)

web_file = r' https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27'
wd.get(web_file)

elements = wd.find_element(By.CLASS_NAME,'songlist__list').find_elements(By.TAG_NAME,'li')

'''
解题方式一：
for element in elements:
	icon_rank_down = element.find_element(By.CLASS_NAME,'songlist__rank').find_element(By.TAG_NAME,'i').get_attribute('class')
	if icon_rank_down == 'icon_rank_down':
		song_name = element.find_element(By.CLASS_NAME,'songlist__cover').get_attribute('title')
		people_name = element.find_element(By.CLASS_NAME,'playlist__author').text

		print(f'{song_name:10} : {people_name}')
'''

# 解题方式二：
for element in elements:
	rank = element.find_element(By.CLASS_NAME,'songlist__rank').find_element(By.TAG_NAME,'i').get_attribute('outerHTML')
	
	if 'icon_rank_down' not in rank:
		continue
	
	# 歌名 song_name
	song_name_str = element.find_element(By.CLASS_NAME,'songlist__cover').get_attribute('outerHTML')
	p = re.compile(r'title=\"(.+?)\"')
	song_name = p.findall(song_name_str)[0]
	
	# 歌手 people_name
	people_name = element.find_element(By.CLASS_NAME, 'playlist__author').text
	print(f'{song_name:<15} : {people_name}')
	
# 关闭
wd.quit()

