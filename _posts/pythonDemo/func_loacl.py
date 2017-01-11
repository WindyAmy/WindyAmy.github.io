#coding=utf-8
#Python 函数局部变量
'''
可以使用global将局部变量变成全局变量
'''

def func(x):
	print 'x is ',x
	x=2
	print 'Changed local x to',x
x=50
func(x)
print 'x is still ',x