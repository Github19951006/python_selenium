"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/31
@File   :yuerwen_03_替换字符串.py
"""
names = '''下面是这学期要学习的课程：
<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律
<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式
<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''

import re
p = re.sub(r'/av\d+/', '/cn345677/',names)
print(p)
print(type(p))  # <class 'str'>