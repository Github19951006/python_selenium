"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/03
@File   :yuerwen_作业.py
"""
'''
1、使用request库获取 html网页

'''
import requests,re,os

from urllib.parse import quote

wget_scr = r'D:\tools\wget'
target_scr = r'http://www.listeningexpress.com/studioclassroom/ad/'

# 1、使用request库获取 html网页
ret = requests.get(target_scr)
# 将request.get类转换成 字符串
content = ret.text

# 正则表达式获取MP3文件地址
p = re.compile(r"javascript:p\('(.*?)'")
# 返回的是一个列表
MP3_list = p.findall(content)

for scr in MP3_list:
	# 字符串拼接
	fullAddr = target_scr + quote(scr)
	# 执行下载文件
	os.system(f'{wget_scr} {fullAddr}')
	
	
