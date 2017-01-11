#coding=utf-8
#字典使用
'''
字典是键值对的关系

字典中的键值对是没有顺序的
字典是dict类的实例对象

for 遍历使用字典的items()方法
是否包含使用has_key('xxx')方法
'''
ab={'Swaroop':'abc@qq.com',
'Larry':'larry@qq.com',
'Windy':'Windy@qq.com'
}
print 'Windy\'s address is %s'%ab['Windy']

for name,address in ab.items():
	print'Contact %s at %s'%(name,address)

if 'Windy' in ab:# OR ab.has_key('Windy')
	print 'Yes Windy is exist'