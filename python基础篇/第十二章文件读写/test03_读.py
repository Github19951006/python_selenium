"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/09
@File   :test03_读.py
"""
#  mode 参数为 r 则读取文件内容
f = open('yuerwen.txt','r',encoding='utf8')
# read 方法会在读取文件中的原始字节串后， 根据上面指定的gbk解码为字符串对象返回
content = f.read(4)
# 通过字符串的split方法获取其中用户名部分
name = content.split('！')[0]
print(name)

