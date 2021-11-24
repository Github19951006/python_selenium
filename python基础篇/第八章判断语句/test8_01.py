"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/07/31
@File   :test8_01.py
    第八章：判断语句
"""

'''
说明：简单的使用if语句，还没使用else 和elif
def regiterUers():
    phone = input("请输入电话号码（不超过11位字符）：")
    if len(phone) > 11:
        print("输入有误，手机号码超过11位")
    print("函数结束！")
'''

'''
# 优化函数
# 使用if...else语句
def regiterUers():
    phone = input("请输入电话号码（不超过11位字符）：")
    if len(phone) > 11:
        print("输入有误，手机号码超过11位")
    else:
        print("手机号码输入正确！")
'''

# 进一步优化函数
def regiterUers():
    # 键入手机号码
    phone = input('请输入电话号码（不超过11位字符）：')
    # 判断函数
    # 判断输入的是不是11位字符
    if len(phone) > 11:
        print("有误！输入的手机号码超过11位")
    # 判断输入是不是数字
    # isdigit() 方法检测字符串是否只由数字组成。  返回值：如果字符串只包含数字则返回 True 否则返回 False。
    elif not phone.isdigit():
        print("有误！输入的不是纯数字")
    # 判断是否以1开头
    elif not phone.startswith('1'):
        print("有误！输入的不是1开头")
    else:
        print("输入的手机号码正确")

# 调用函数
regiterUers()