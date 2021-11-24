"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/03
@File   :yuerwen_08_字符串替换sub.py
"""

# 需求：找到所以 /avxxxxxx/ 这种 以 /av 开头  这些字符串全部 替换为 /cn345677/
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

'''
第一个参数，表示正则表达式的式子
第二个参数，这里 是 '/cn345677/' 这个字符串，表示用什么来替换。
第三个参数是 源字符串。
'''
new_str = re.sub(r'/av\d+?/','/cn345677/',names)
print(new_str)
