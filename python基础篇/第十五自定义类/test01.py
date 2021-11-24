"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/26
@File   :test01.py
"""
'''
总结：
1、静态方法 @staticmethod
使用：类名.静态方法()

2、初始化方法 __init__(self,参数)
使用：类名(参数)
默认是初始化实例的时候就调用该方法，记得传入参数

3、自定义方法
使用:类的实例名称.方法名(参数)

'''
class Car:
    bran = '汽车'
    country = '中国'
    
    # 类的静态方法
    @staticmethod
    def perq():
        # return '嘟嘟'
        print("发放")
    
    # 初始化的 类的实例属性
    '''
    理解：类 实例化出来的实例
         不同实例各自具备的属性，就是类的实例属性
         通常实例属性 在类的初始化方法__init__(self) 里面定义
         def __init__(self,参数)
         
         初始化方法在实例化调用的时候就执行的
    '''
    def __init__(self,col,esn):
        self.color = col
        self.enginSn = esn
        
    # 类的实例 属性  改变颜色
    # 自定义的 类的实例方法
    def changeColor(self,newColor):
        self.color = newColor
        
    
# 创建实例
BYD = Car('黑色','8979umn90')
# BYD = Car()
print(BYD)   # <__main__.Car object at 0x00000218EA41F100>
print(f'汽车的颜色：{BYD.color}')
print(f'发动机编号：{BYD.enginSn}')
BYD.changeColor('红色')
print(f'change汽车的颜色：{BYD.color}')
print(Car.perq())