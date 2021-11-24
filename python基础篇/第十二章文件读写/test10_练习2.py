"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/11
@File   :test10_练习2.py
"""
'''
题目2
你们公司有一批图片文件，不小心被管理人员把扩展名都去掉了。
这批图片文件中有的是png文件，有的是jpg文件。
png文件的开头一定是 这样的 89 50 4e 47 0d 0a 1a 0a 8个字节
现在要求你写一个函数，参数是图片文件的路径，函数根据文件的开头8个字节的信息，判断该文件是不是png文件。
如果是，打印出 png， 否则打印出 jpg。
'''
def tellPngFile(fp):
    # 使用字节串读取文本信息
    with open(fp,'rb') as f:
        # 使用字节串读取
        numberF = f.read(8)
        # 判断
        if numberF == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
            print('png文件')
        else:
            print('非png文件')

tellPngFile('1.png')
