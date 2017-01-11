#coding=utf-8
#模块的使用
'''
如果在其他程序重用很多函数，就需要使用模块

.pyc是python 的字节编译文件。
Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成
计算机使用的机器语言并运行

导入模块方式：
1、import 模块名称（建议使用）
  import sys
2、from 模块 import 函数
  from sys import argv
'''
import sys

print 'The command line arguments are:'
for i in sys.argv:
	print i
print '\n\n The python path is ',sys.path,'\n'
