"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/03
@File   :yuerwen_09_指定函数替换.py
"""

import re

names = '''

下面是这学期要学习的课程：

<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律

<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式

<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''


# 替换函数，参数是 Match对象
def subFunc(match):
	# Match对象 的 group(0) 返回的是整个匹配上的字符串，
	src = match.group(0)
	
	# Match对象 的 group(1) 返回的是第一个group分组的内容
	number = int(match.group(1))+6

	# 字符串的格式化拼接
	dest = f'/av{number}/'
	print(f'{src} 替换为 {dest}')
	
	# 返回值就是最终替换的字符串
	return dest

newStr = re.sub(r'/av(\d+?)/', subFunc, names)
print(newStr)