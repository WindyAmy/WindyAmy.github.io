#coding=utf-8
#类的__init__方法
'''
__init__类似构造函数
'''

class Person:
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name=name
	def sayHi(self):
		print 'Hello,my name is',self.name

p=Person("Windy")
p.sayHi()
