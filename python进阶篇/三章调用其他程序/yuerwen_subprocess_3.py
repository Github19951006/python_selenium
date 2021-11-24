"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/01
@File   :yuerwen_subprocess_3.py
"""
# subprocess模块提供了更多调用外部程序的功能；
from subprocess import PIPE,Popen

# 返回的是 Popen 实例对象
proc = Popen(
    'fsutil volume diskfree c:',
    stdin  = None,
    stdout = PIPE,
    stderr = PIPE,
    shell=True)

# 返回的是一个元组
# communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# 标准输出设备和 标准错误设备 当前都是本终端设备
outinfo, errinfo = proc.communicate()

# 注意返回的内容是bytes 不是 str ，我的是中文windows，所以用gbk解码
outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')
print (outinfo)
print ('-------------')
print (errinfo)

# 按行切割，然后存储到列表中
outputList = outinfo.splitlines()
# print(outputList)

# 剩余量
free  = int(outputList[0].split(':')[1].split(' (')[0])

# 总空间
total = int(outputList[1].split(':')[1].split(' (')[0])

if (free/total < 0.1):
    print('!! 剩余空间告急！！')
else:
    print('剩余空间足够')