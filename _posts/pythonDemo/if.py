#coding=utf-8
#Python 控制流程
'''
1、if
2、while
3、for
4、break
5、continue

python 没有switch

while 循环 有一个可选的else从句
'''

number=23
guess=raw_input('Enter an integer:')
if guess==number:
	print 'Congratulations,you guessed it'
	print ''
	pass
elif guess<number:
	print 'it is a little higther than that'
else:
	print 'No,it is a little lower than that'
print 'Done'