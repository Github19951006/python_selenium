"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/21
@File   :yuerwen_selenium_选择元素_附加练习1.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
找出其中排名上升的歌曲和演唱者
最终结果显示的结果如下：

孤独                ： G.E.M. 邓紫棋
Lovesick Girls      ： BLACKPINK
落幕人              ： 任然
幸存者              ： 林俊杰
刁钻                ： 任然
'''

# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
webDriver = webdriver.Chrome()

# 设置等等时间
webDriver.implicitly_wait(5)

# 根据webdriver对象的get方法 打开指定的web地址
web_file = r' https://y.qq.com/n/ryqq/toplist/27'
webDriver.get(web_file)

songlist_element = webDriver.find_element(By.CLASS_NAME,'songlist__list')
li_elements = songlist_element.find_elements(By.TAG_NAME,'li')

for li in li_elements:
	rank_up_element =li.find_element(By.TAG_NAME,'i')
	if rank_up_element.get_attribute('class') == 'icon_rank_up':
		# 歌名
		son_name = li.find_element(By.CLASS_NAME,'songlist__songname_txt').text
		# 歌手
		son_author = li.find_element(By.CLASS_NAME, 'playlist__author').text

		print(f"歌名:{son_name:20}  歌手:{son_author}")

webDriver.quit()