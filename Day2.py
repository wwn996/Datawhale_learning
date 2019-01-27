#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
一、今日学习任务
----------------------------------------------------------------
【Day 2】
1. 基础
(1)列表
标志
基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
列表相关方法
(2)元组
标志
基本操作（创建及不可变性）
2. 提升
序列类型，相互转换及方法
【作业构想】
学习代码200-300行
定义一个列表，包含自己的家庭成员，，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
----------------------------------------------------------------
'''

# 二、自学及实践内容
# 
# 1. 基础
# 1.1 列表
# 1.1.1概念：是用来处理一组有序项目的数据结构。列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 注意：列表的数据项不需要具有相同的类型。创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

# 1.1.2 列表的基本操作
# 1.1.2.1 创建:创只要把逗号分隔的不同的数据项使用方括号（[ ]）括起来即可 下标（角标，索引）从0开始，最后一个元素的下标可以写-1
list1 = ['test1', 'test2', 'test3', 2019, 2020]
list２ = ["a", "b", "c", "d"]
list３ = []  # 创建一个空列表
type(list1)  # 查询list1的类型

# 1.1.2.2 添加 
# list.append()  # 在list 末尾增加一个元素
# list.insert（n,'4'） # 在指定位置添加元素，如果指定的下标不存在，那么就是在末尾添加
# list1.extend(list2)  # 合并两个list，list2中仍有元素
list4 = ['Google', 'Runoob', 'Taobao']
list5 = ['Amazon']

list4.append('Baidu')
print ("更新后的列表：", list4)

list4.insert(1, 'Microsoft')
print("第二次更新后的列表：", list4)

list4.extend(list5)
print("第三次更新后的列表：", list4)

# 1.1.2.3 删除
# list.pop() 删最后一个元素
# list.pop(n)指定下标，删除指定的元素，如果删除一个不存在的元素会报错
# list.remove(xx) 删除list 里面的一个元素，有多个相同的元素，删除第一个 
# del 可进行任何删除，可删除对象，非列表内方法
list6 = ['test1', 'test2', 'test3', 'test4', 'test5']
list6.pop()
print("第一次删除后的列表： ",list6)

list6.pop(0)
print("第二次删除后的列表： ",list6)

list6.remove('test3')
print("第三次删除后的列表： ",list6)

del list6[0]
print("第四次删除后的列表： ",list6

# 1.1.2.4 深浅拷贝
# 参考资料：https://www.cnblogs.com/pyramid1001/p/5844905.html
# 区别：
# （1） copy() 浅拷贝只能拷贝最外层，修改内层则原列表和新列表都会变化。
# （2）copy.deepcopy（）深拷贝是指将原列表完全克隆一份新的。
# 
# 浅拷贝：
names = ['小明', '小红', '小黑', '小黄', '小白']
names2 = names.copy()
print(names)
print(names2)

names[3] = "Yellow"
print(names)
print(names2)

# 深拷贝
import copy
names = ['小明', '小红', '小黑', ['粉色'], '小黄', '小白']
names3 = copy.deepcopy(names)
names3[3][0] = 'Pink'
print(names)
print(names3)

# 1.1.2.5 更新
list7 = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list7[2])
list7[2] = 2001
print ("更新后的第三个元素为 : ", list7[2])

# 1.1.2.6 查询
list7    遍历列表

# 1.1.3 列表相关方法
# 1.1.3.1 Python列表脚本操作符
len([1, 2, 3])  # 获取列表的长度
[1, 2, 3] + [4, 5, 6]  # 列表的组合
['Hi!'] * 4  # 列表重复4次
3 in [1, 2, 3]  # 查询元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")  # 迭代

# 1.1.3.2 Python列表截取与拼接
list8 = ['test1', 'test2', 'test3', 'test4', 'test5']
list8[2]  # 读取第三个元素
list8[-2]  # 从右侧开始读取倒数第二个元素: count from the right
list8[1:]  # 输出从第二个元素开始后的所有元素
list8[1:5]  # 输出从第二个元素到四个元素的所有元素，切片是不包含后面那个元素的值（顾头不顾尾）
list8[:4]  # 输入从第一个元素到第三个元素的所有元素；如果切片前面一个值缺省的话，从开头开始取
list8[:]  # 如果全部缺省，取全部
list8[0:4:2]  # list[n:m：s]  s:步长，隔多少个元素取一次

list9 = [1, 2, 3, 4]  # 拼接操作
list9 += [5, 6, 7, 8]
print(list9)

# 1.1.3.3 嵌套列表
a = [1, 2, 3]
b = [4, 5, 6]
c =[a, b]
print(c)
print(c[0][1])

# 1.1.3.4 Python列表函数&方法
list10 = ['a', 'b', 'c', 'd', 'e', 'a']
len(list10)  # 列表元素个数 
max(list10)  # 返回列表元素最大值 
min(list10)  # 返回列表元素最小值 
list10.count('a')  # 统计某个元素在列表中出现的次数
list10.index('b')  # 从列表中找出某个值第一个匹配项的索引位置
# list(seq)  # 将元组转换为列表

list10.reverse()  # 反向列表中元素
print(list10)

list10.sort()  # 排序，默认升序
print(list10)

list10.sort(reverse=True)  # 降序排列
print(list10)

# enumerate  # 用法（打印元素对应的下标）
list11 = ['a', 'b', 'c']
for i, v in enumerate(list11): 
	print('index = %s, value = %s '%(i,v))


# ----------------------------------------------------------------
#
# 1.2 元组
# 1.2.1 元组的概念
# （1）Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# （2）元组使用小括号，列表使用方括号。
# （3）元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# 1.2.2基本操作（创建及不可变性）
# 1.2.2.1 创建
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
tup4 = ()  # 空元组
type(tup3)

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup5 = (50)
type(tup5)     # 不加逗号，类型为整型

tup6 = (50,)
type(tup6)     # 加上逗号，类型为元组

# 1.2.2.2 拼接
# 注意：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (1, 2, 3)
tup2 = ('test1', 'test2', 'test3')
tup3 = tup1 + tup2
print(tup3)

# 1.2.2.3删除
# 注意：元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup7 = [1, 2, 3]
del tup7

# 1.2.2.4 访问
# 元组可以使用下标索引来访问元组中的值
tup8 = ['test1', 'test2', 'test3', 'test4']
print(tup8[0])
print(tup8[0:3])

# 1.2.3 元组运算符
len((1, 2, 3))  # 计算元素个数
(1, 2, 3) + (4, 5, 6)  # 连接
('Hi!',) * 4  # 复制
3 in (1, 2, 3)  #元素是否存在
for x in (1, 2, 3): print (x,)　　# 迭代 

# 1.2.4 元组索引，截取
L = ('Google', 'Taobao', 'Runoob', 'Baidu')
L[2]  #　读取第三个元素
L[-2]　　#　反向读取；读取倒数第二个元素
L[1:]　　#　截取元素，从第二个开始后的所有元素。

# 1.2.5 元组内置函数
# len(tuple)  # 计算元组元素个数。
# max(tuple)  #返回元组中元素最大值。
# min(tuple)  # 返回元组中元素最小值。
# tuple(seq)  #将列表转换为元组。

# 1.2.6 元组不可变性
# 元组的不可变性其实是指的是tuple数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。
# 元组的值会随着引用的可变对象的变化而变。元组中不可变的是元素发标识。
a = (1,2)
a[0] = 2  # 会报错TypeError: 'tuple' object does not support item assignment。
a1 = (1,2,[1,2,3])
a1[2][1] = 0  # 是可以的，不会报错

# ----------------------------------------------------------------
#
# 2. 提升
# 2.1 序列类型，相互转换及方法
# 序列类型包括字符串类型、列表类型、元组类型
# 
# (1)list转换为string或tuple
li = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
sli = str(li)
print(sli)
tli = tuple(li)
print(tli)

# (2)string转换为lsit或tuple
s = 'hello, world!'
ls = list(s)
print(ls)
ls1 = s.split(',')
print(ls1)
ts = tuple(s)
print(ts)

# (3)tuple转换成string或list
tu = (1, 2, 3, 4, 'a', 'b', 'c', 'd')
stu = str(tu)
print(stu)
ltu = list(tu)
print(ltu)

# ----------------------------------------------------------------
#
# 三、作业
# 定义一个列表，包含自己的家庭成员，，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
# 创建列表
list = ['father','mother', 'sister', 'brother']
list1 = ['uncle', 'anut', 'cousin']
# 添加
list.append('boyfriend')
list
list.insert(5, 'girlfriend')
list
# 修改
list[5] = 'friend'
list
# 删除
list.pop()
list
del list[4]
list 
# 列表拼接
list2 = list + list1
# 查询
list2
list2[2]

