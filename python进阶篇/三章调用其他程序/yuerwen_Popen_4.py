"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/02
@File   :yuerwen_Popen_4.py
"""
# 调用外部程序 方式有两种：
# 1、os.system()
# 2、Poen 方法
# 区别：os.system 它会等待外部程序运行结束后再执行其他的代码；Poen 方法是不要等待外部程序运行结束后再执行其他的代码
from subprocess import Popen,PIPE
import time,sys,os
import os
# 所以需要双引号括起来，这是Windows shell的语法
notepadexepath = r'"D:\tools\notapad++\Notepad++\notepad++.exe"'

# 当前代码文件的路径
scriptpath = r'D:\study\python\python进阶篇\三章调用其他程序\yuerwen_01.py'

# 调用notepad++ 打开 当前代码文件
cmd = f'{notepadexepath} {scriptpath}'

# os.system(cmd)
popen = Popen(
	# args:表示路径
	args = cmd,
	shell = True
)
#
time.sleep(2)

# 返回一个Popen实例对象
objectPopen = Popen(
	'tasklist',
	stdin = None,
	stdout = PIPE,
	stderr = None,
	shell= True
)

# communicate 方法返回 输出信息
outinfo,errinfo = objectPopen.communicate()

# 对返回来的字节码对象进行解码 decode
outinfo = outinfo.decode('gbk')
print(type(outinfo))  # <class 'str'>

pid = None
outList = outinfo.splitlines()
for pinfo in outList:
	if 'notepad++.exe ' in pinfo:
		print(pinfo)
		
		pinfoList = pinfo.split(' ')
		
		# 去掉其中的空字符串元素
		infolist = [info for info in pinfoList if info]
		print(infolist)
		# 获取进程pid
		pid = infolist[1]
		print(f'notepad++.exe的进程pid：{pid}')
		break

# 如果pid为空
if pid is None:
	print('对不起，没有发现notepad++的进程ID')
	sys.exit(2)


# 总结：
# 如果是要到网页等地方
# 执行shell 命令
os.system(f'taskkill /PID {pid} /F')

print('打印结束！')