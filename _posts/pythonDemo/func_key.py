#coding=utf-8
#关键参数
'''
如果你的某个函数有许多参数，而你只想指定其中的一部分，那么
可以使用命名来为这些参数赋值----这被称作关键参数
使用名称而不是位置来给函数指定实参
'''

def func(a,b=5,c=10):
	print 'a is ',a,'and b is ',b,'and c is ',c
func(3,7)
func(25,c=24)
func(c=50,a=100)