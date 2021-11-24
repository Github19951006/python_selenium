"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/09
@File   :test02_追加写.py
"""
#  mode 参数为 a  则会追加在文件内容的最后
# 1、打开文件，指定编码方式
f = open('yuerwen.txt','a',encoding='utf8')
# 2、write方法将字符串编码为utf8字节写入文件
f.write('yuerwen,加油！！')
# 关闭文件流
f.close()