"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/01
@File   :test8_02.py
        第八章：判断语句2
"""
# 使用if 结合return语句
def registarUers():
    phone = input("请输入手机号码（不超过11位）：")
    # 对输入的手机号码进行判断
    #1 判断语句手机号长度是的大于11位字符
    if len(phone) > 11:
        print("有误，您输入的手机号码大于11位")
        return
    #2 判断是否是以1开头
    if not phone.startswith('1'):
        print("有误，您输入的手机号码不是以1开头")
        return
    #3 判断是否是纯数字组成
    if not phone.isdigit():
        print("有误，您输入的手机号码不是纯数字组成")
        return
    else:
        print("您输入的手机号码正确")

registarUers()