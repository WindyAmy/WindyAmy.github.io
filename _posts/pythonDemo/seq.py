#coding=utf-8
#序列
'''
序列有两个特点 索引操作符及切片操作符
切片获取序列的一部分
序列可以是正数或者负数（从后往前获取）

切片：shoplist[1:3] 返回从位置1开始，包括位置2，但是停止的位置3的一个序列切片
及包含左边不包含右边的值

注意：如果需要复制一个列表或者类似对应，你必须使用切片炒作来取得拷贝
'''
shoplist=['apple','magngo','carrot','banana']

#Indexing or Subscription operation

print 'Item 0 is',shoplist[0]

print 'Item 1 is',shoplist[1]
print 'Item 2 is',shoplist[2]
print 'Item 3 is',shoplist[3]
print 'Item -1 is',shoplist[-1]
print 'Item -2 is',shoplist[-2]

#Slicing on a list
print 'Item 1 to 3 is ',shoplist[1:3]
print 'Item 2 to end is ',shoplist[2:]
print 'Item 1 to -1 is',shoplist[1:-1]
print 'Item start to end is',shoplist[:]

#Slicing on a string 
name='swaroop'
print 'characters 1 to 3 is ',name[1:3]
print 'characters 2 to end is',name[2:]
print 'characters 1 to -1 is',name[1:-1]
print 'characters start to end is',name[:]