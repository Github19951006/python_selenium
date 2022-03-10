"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2021/12/20
@File   :yuerwen_selenium_QQ音乐排名_附加练习3.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
# chrome驱动器 地址
webdriver_file = Service(r'd:\webdrivers\chromedriver.exe')
# 创建webdriver 对象 指明Chrome驱动器地址
wd = webdriver.Chrome(service=webdriver_file)

# 等待时间
wd.implicitly_wait(5)

web_file = r'https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27'
wd.get(web_file)
#
# wb_element = wb.find_element(By.CLASS_NAME,'songlist__list')
# # 歌名
# names = wb_element.find_elements(By.CLASS_NAME, 'songlist__cover')
# # for ee in names:
#     # print(ee.accessible_name)
#
# # # 歌手名字
# w = wb_element.find_elements(By.CLASS_NAME,'icon_rank_up')
# for e in w:
#     if e.get_attribute('class') == 'icon_rank_up':
#         pass
#         # 歌名
#         # name = wb_element.find_element(By.CLASS_NAME, 'songlist__cover')
#         # print(name.text)
#         # # 歌手名字
#         # name1 = wb_element.find_element(By.CLASS_NAME, 'playlist__author')
#         # print(name1.text)
#所有歌曲
elements = wd.find_element(By.CLASS_NAME,'songlist__list').find_elements(By.CSS_SELECTOR,'li')
comment_list = []
list2 = []
list3 = []
for element in elements:
    rank = (element.find_element(By.CLASS_NAME,'songlist__rank')).find_element(By.TAG_NAME,'i')
    if rank.get_attribute('class') == 'icon_rank_up':
        song = element.find_element(By.CLASS_NAME,'songlist__cover')#上升 歌曲名
        name = (element.find_element(By.CLASS_NAME,'playlist__author')).get_attribute('title')#上升 歌手名
        print(f'{song.accessible_name:10}： {name}')
        list2.append(song.accessible_name)
        list3.append(name)
comment_list.extend(list2)
new_list = [[x] for x in comment_list]
headers = ['no','name']
with open('tets1.csv','w',newline='',encoding='utf-8') as fp :
    # 获取对象
    writer_obj = csv.writer(fp)
    # 写入数据
    writer_obj.writerow(headers)
    # 写入数据
    for i in new_list:
        writer_obj.writerow(i)



# 关闭
wd.quit()