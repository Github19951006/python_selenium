"""
@Project ：python
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/26
@File   :yuerwen_08_练习.py
"""
from threading import Thread
import os

wget_path = r'd:\tools\wget.exe'

def wget_download(url):
	os.system(f'{wget_path} {url} -p d:\\tmp')

while True:
	url = input('请输入下载网址：')
	
	if url.strip() == '':
		continue
	
	thread = Thread(target=wget_download,args=(url,))
	thread.start()