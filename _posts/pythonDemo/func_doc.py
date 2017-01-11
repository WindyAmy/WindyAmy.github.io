#coding=utf-8
#DocStrings
'''
python 特性
文档字符串

1、在函数的第一个逻辑行的字符串是这个函数的文档字符串 适用于，模块和类
2、文档字符串是一个多行的字符串
首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述
3、通过使用__doc__
'''

def printMax(x,y):
	# this is doc
	'''prints the maximum of two numbers.
	The two values must be integers.'''

	x=int(x);
	y=int(y);
	if x>y:
		print x,'is maximum'
	else:
		print y,'is maximum'
printMax(3,5)
print printMax.__doc__