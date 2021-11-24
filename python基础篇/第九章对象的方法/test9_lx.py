"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/03
@File   :test9_lx.py
"""
'''
请写一个程序：

首先提示用户输入年龄、身高、体重信息，格式如下如下

请输入您的性别：男
请输入您的身高（厘米）：175厘米
请输入您的体重（公斤）：80公斤
注意：

用户输入的内容，前后、中间都可能有空格，比如 175 厘米

然后根据如下的计算公式，计算出身高对应的标准体重。

标准体重(男)=(身高cm-100)x0.9(kg)
标准体重(女)=(身高cm-100)x0.9(kg)-2.5(kg)
如果体重在标准体重上下5公斤，都属于标准体重，提示用户体重标准。

否则提示用户高于标准还是低于标准
'''
sex = input("请输入您的性别：")
# 空格处理
retSex = sex.replace(' ','')

height = input('请输入您的身高（厘米）：')
# 空格处理
retHeight = height.replace(' ','')
retHeight = float(height.replace('厘米',''))

weight = input('请输入您的体重（公斤）：')
# 空格处理
retWeight = weight.replace(' ','')
retWeight = float(weight.replace('公斤',''))

if retSex == '男':
    bPip = (retHeight - 100)*0.9
else:
    bPip = ((retHeight - 100) * 0.9) - 2.5

if bPip - 5 < retWeight < bPip + 5:
    print('您的体重标准')
elif bPip < retWeight:
    print('您的体重高于标准')
else:
    print('您的体重低于标准')
