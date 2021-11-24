"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/10
@File   :test06_copy.py
"""
'''
如何字节实现一个简单的文件拷贝功能呢？
实现一个函数，有两个参数，第一个参数是源文件路径，第二个参数是拷贝生成的目标文件路径。
'''
def getCopy(srcPath,descPath):
    # 打开文件
    fRead = open(srcPath,'rb')
    # 读字符串，返回一个字节串
    content = fRead.read()
    # 关闭文件流
    fRead.close()

    # 打开文件
    fWrite = open(descPath,'wb')
    # 拿到字节串，写入文件
    fWrite.write(content)
    # 关闭文件流
    fWrite.close()

getCopy('yuerwen.txt','descyuerwen.txt')