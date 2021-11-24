"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/11
@File   :test11_附加练习.py
"""
'''
题目要求：
解压该压缩包，里面 包含了两个文件。 一个叫 ‘gbk编码.txt’,该文件是gbk编码的。
另一个文件叫 ‘utf8编码.txt’, 该文件是utf8编码的。
两个文件里面的内容都包含中文。
要求大家编写一个python程序，该程序做到以下2点
1、将两个文件内容读出， 合并内容到一个字符串中， 并能用print语句将合并后的内容正确显示
2、然后，程序用中文提示用户“请输入 新文件的名称请输入 新文件的名称”， 用户输入文件名可以包含中文 将上面合并后的内容存储到一个新文件中，以utf8格式编码。 新文件的文件名就是上面用户输入的名字。
'''


# 创建一个列表存储合并内容到一起的内容
listLine = []
'''
getFile(文件路径)方法：
将两个文件内容读出，合并内容到一个字符串中，并能用print语句将合并后的内容正确显示
返回一个列表
'''
def getFile(strFile):
    # 打开文件，读取字节串
    with open(strFile,'rb') as f:
        # 以字节串读取，返回的是字节串
        content = f.read()
        # 判断文件的字符编码
        # 对文件名进行分割获取，判断对象
        if strFile.split(".")[0] == 'gbk编码':
            # 字节串以 gbk解码,返回字符串
            content = content.decode('gbk')
        else:
            # 字节串以 utf8解码,返回字符串
            content = content.decode('utf8')
        # 字符串 追加到列表最后
        listLine.append(content)
        # 返回列表
    return listLine
'''
getCopy(文件路径)方法：
提示用户“请输入 新文件的名称”，用户输入文件名可以包含中文，将上面合并后的内容存储到一个新文件中，以utf8格式编码
'''
def getCopy(descPath):
    # 打开文件,指定文件编码为utf8
    with open(descPath,'w',encoding='utf8') as fWrite:
        # 拿到字符串，写入文件
        fWrite.write(StrlistLine)

# 调用函数
gbk = getFile('gbk编码.txt')
utf8 = getFile('utf8编码.txt')
# 将列表转换成字符串
StrlistLine = ','.join(utf8)
print(StrlistLine)
# 键入文件名称
newName = input('请输入 新文件的名称：')
getCopy(newName)
