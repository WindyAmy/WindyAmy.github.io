#coding=utf-8
#类
'''
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是
在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本
身，按照惯例它的名称是self。
如：
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
'''

class Person:
	pass#我们使用了一个空白块，它由pass语句表示
p=Person()
print p
