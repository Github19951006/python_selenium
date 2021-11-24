"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/21
@File   :yuerwen_附加练习.py
"""
videoFiles = '''
bandicam 2020-01-06 11-00-45-494.mp4
bandicam 2020-01-06 11-01-35-020.mp4
bandicam 2020-01-06 11-05-11-334.mp4
'''

ffmpegEXE = r'D:\ffmpeg.exe'

import os

inputfiles = [line for line in videoFiles.splitlines() if line.strip()]


def handle(inputfile):
	print(f'=====>{inputfile}')
	
	cmd = f'{ffmpegEXE} -i "{inputfile}" -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy "mp_{inputfile}"'
	os.system(cmd)


for inputfile in inputfiles:
	handle(inputfile)

input('\n=== 转化完成 ===')