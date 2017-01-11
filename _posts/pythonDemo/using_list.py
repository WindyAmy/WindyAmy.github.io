#coding=utf-8
#列表使用
'''
python 列表
append（）
sort() 
del 删除

list[0] 下标访问
'''
#This is my shopping list
shoplist=['apple','mango','carrot','banana']
print 'I hava ',len(shoplist),'items to purchase.'
print 'Thess itesm are:'
for item in shoplist:
	print item,
shoplist.append('rice')
shoplist.sort()
print '\n sort list is ',shoplist

print 'The first item I will buy is',shoplist[0]

del shoplist[0]

print 'The first item I will buy is',shoplist[0]