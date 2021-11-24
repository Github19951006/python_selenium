"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/04
@File   :yuerwen_附加作业.py
"""
'''
下载zip包，解压后出现一个 prac_re 目录，该目录中有很多文件。
请写代码，检查目录中所有文件，找出包含如下格式的文本
https://www.bilibili.com/video/av74106411/?p=60
将数字的值改为 +3， 比如，上面的链接就需要改为
https://www.bilibili.com/video/av74106411/?p=63
如果链接后面的是 p=1 就要改为 p=4, 是 p=99 就要改为 p=102,
最后将修改结果写回文件。
'''
import os,re

def sub_list(match):
   scr = match.group(0)
   # Match对象 的 group(1) 返回的是第一个group分组的内容
   number = int(match.group(1)) + 3
   dest = f'/av74106411/?p={number}'
   print(f'{scr} 替换为 {dest}')
   # 返回值就是最终替换的字符串
   return dest

# 目标路径
path = 'prac_re'
   # 递归的遍历目录下面所有的文件
   # 下面的三个变量 dirpath, dirnames, filenames
   # dirpath 代表当前遍历到的目录名
   # dirnames 是列表对象，存放当前dirpath中的所有子目录名
   # filenames 是列表对象，存放当前dirpath中的所有文件名
for (dirpath,dirname,filesname) in os.walk(path):
   for filename in filesname:
      # filename是代表文件的名称
      # os.path.join 是文件路径的拼接
      fpath = os.path.join(dirpath,filename)
      # utf8编码 读取文件
      with open(fpath,'r',encoding='utf8') as f:
	      # splitlines() 是按换行符切割，得到一行行的元素存储到列表中
	      flist = str(f.read().splitlines())
	      newStr = re.sub(r'\/av74106411\/\?p=(\d*)', sub_list, flist)
	      
	      # 6、通过w写入文件中
	      with open(fpath, 'w', encoding='utf') as f1:
		      f1.write(newStr)

