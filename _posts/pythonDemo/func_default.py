#coding=utf-8
#函数的默认值
'''
默认参数使用的是=给参数赋值

注：只能在参数末尾使用默认参数
def func(a,b=5) 有效
def func(a=5,b) 无效
'''

def say(message,times=1):
	print message*times

say('Hello')
say('World',5)

