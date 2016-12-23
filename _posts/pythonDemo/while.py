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
running=True
number=23
while running:
	guess=int(raw_input('Enter an integer:'))
	if guess==number:
		print 'Congratulations,you guessed it'
		running=False
		pass
	elif guess<number:
		print 'it is a little higther than that'
	else:
		print 'No,it is a little lower than that'
else:
	print 'this is while end'
print 'Done'