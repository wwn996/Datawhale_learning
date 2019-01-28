#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
一、今日学习任务
----------------------------------------------------------------
【Day 3】
【dict字典】
定义
创建
字典的相关方法
-----------------------------------
【set集合】
特性
创建
方法
-------------------------------------
【file文件读取】
 打开文件方式（读写两种方式）
文件对象的操作方法
*学习对excel及csv文件进行操作*
**内容为选做内容，可根据自己基础决定是否做此内容
--------------------------------------
【作业构想】
学习代码200-300行
读取一个文件【文件将在之后给出】，将文件中转换为字典，key值为学习项目，value值为一个负责人列表，并判断字典中是否有负责人负责多个学习项目。
-------------------------------------
"""

# 二、自学及实践内容

# 1. 字典
# 1. 定义
# (1)字典是另一种可变容器模型，且可存储任意类型对象。
# (2)字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
# d = {key1 : value1, key2 : value2 }
"""
注意：
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""

# 1.2 字典的相关操作
# 1.2.1 创建字典
dict1 = {'testA': '1995', 'testB': '1996', 'testC': '1997'}
dict2 = {'abc': 123, 98.6: 37}
# ----------------------------------------------------------------------
# 1.2.2 访问字典里的值
# (1)把相应的键放入到方括号中
# (2)如果用字典里没有的键访问数据，会输出错误
dict3 = {'Name': 'Cynthia', 'Sex': 'girl', 'Age': 24}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
# ----------------------------------------------------------------------
# 1.2.3 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict4 = {'Name': 'Cynthia', 'Sex': 'Girl', 'Age': 24}
dict4['Age'] = 20  # 修改数据
dict4['Interest'] = 'Sing'  # 添加数据
print("dict4['Age']is: ", dict4['Age'])
print("dict4['Interest']is: ", dict4['Interest'])
# ----------------------------------------------------------------------
# 1.2.4 删除字典元素
# (1)能删单一的元素也能清空字典，清空只需一项操作。
# (2)显示删除一个字典用del命令
alien_0 = {'color': 'green', 'points': 5, 'size': 6}
print(alien_0)
del alien_0['points']  # 删除键'points'
print(alien_0)
alien_0.clear()  # 清空字典
# ----------------------------------------------------------------------
# 1.2.5 遍历字典
# 遍历字典的方式：可遍历字典的所有键—值对、键或值。
# 注意：即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
# 1.2.5.1 遍历所有的键—值对
user_1 = {
    'name': 'Cynthia',
    'sex': 'girl',
    'interest': 'sing'
}
for key, value in user_1.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 1.2.5.2 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# 1.2.5.3 按顺序遍历字典中的所有键
# 要以特定的顺序返回元素，一种办法是在for 循环中对返回的键进行排序。为此，可使用函数sorted() 来获得按特定顺序排列的键列表的副本
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 1.2.5.4  遍历字典中的所有值
# 获取字典包含的值，可使用方法values() ，它返回一个值列表，而不包含任何键。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# ----------------------------------------------------------------------
# 1.2.6 嵌套
# 定义：需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套 。
# 1.2.6.1 字典列表
# 方法：创建一个列表，其中每一项都是一个字典，包含有关的各种信息
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 1.2.6.2 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# 1.2.6.3 在字典中存储字典
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
},
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
},
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
location = user_info['location']
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())
# ----------------------------------------------------------------------
# 1.2.7 字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# (1)不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# (2)键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# ----------------------------------------------------------------------
# 1.2.8 字典内置函数
dict5 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
len(dict5)  # 计算字典元素个数，即键的总数。
str(dict5)  # 输出字典，以可打印的字符串表示。
type(dict5)  # 返回输入的变量类型，如果变量是字典就返回字典类型。
# ----------------------------------------------------------------------
# 1.2.9 字典相关方法
# 详情可参考【菜鸟教程】：http://www.runoob.com/python3/python3-dictionary.html

# 2. 集合（set）
# 2.1 定义：
# (1)集合（set）是一个无序的不重复元素序列。
# (2)可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
parame = {value01,value02,...}
或者
set(value)
"""
# 创建集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 2.2集合的基本操作
# 2.2.1 添加元素
# s.add(x)
test = set(('test1', 'test2', 'test3'))
test.add('test4')
print(test)
# s.update(x)
test1 = set(('test1', 'test2', 'test3'))
test1.update({1, 3})
print(test1)
test1.update([1, 4], [5, 6])
print(test1)
# ----------------------------------------------------------------------
# 2.2.2 移除元素
# s.remove(x) 【注意：将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误】
test2 = set(('test1', 'test2', 'test3'))
test2.remove('test3')
print(test2)
# s.discard(x)  【移除集合中的元素，且如果元素不存在，不会发生错误。】
test2.discard('test3')
print(test2)
# s.pop()  【可以设置随机删除集合中的一个元素】
test3 = test2.pop()
print(test3)
# ----------------------------------------------------------------------
# 2.2.3 计算集合元素个数
# len(s)
test4 = set(("Google", "Runoob", "Taobao"))
len(test4)
# ----------------------------------------------------------------------
# 2.2.4 清空集合
# s.clear()
test5 = {'chinese', 'math', 'english', 'history'}
test5.clear()
print(test5)
set()
# ----------------------------------------------------------------------
# 2.2.5 判断元素是否在集合中存在
# x in s 【判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。】
thisset = set(("Google", "Runoob", "Taobao"))
"Runoob" in thisset
thisset1 = set(("Google", "Runoob", "Taobao"))
"Facebook" in thisset1

# 2.3 集合内置方法完整列表
# 详情可参考【菜鸟教程】：http://www.runoob.com/python3/python3-set.html


# 3. file文件读取
# 3.1 打开文件方式（读写两种方式）
# open() 方法
# Python open()方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出OSError。
# 注意：使用open()方法一定要保证关闭文件对象，即调用close()方法。
# open()函数常用形式是接收两个参数：文件名(file)和模式(mode)。
"""
open(file, mode='r')
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式【t-文件模式，x-写模式，b-二进制模式，+-打开一个文件进行更新（可读可写），r-只读方式打开文件，w-写入文件，a-追加追加】
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
"""
test = open('homework.txt', mode='r+')  # 文件的读写

# 3.2 file对象
# file.close()  # 关闭文件。关闭后文件不能再进行读写操作。
# file.flush()  # 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno()  # 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty()  # 如果文件连接到一个终端设备返回 True，否则返回 False。
# file.next()  # 返回文件下一行。
# file.read([size])  # 从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size])  # 读取整行，包括 "\n" 字符。
# file.readlines([sizeint])  # 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence])  # 设置文件当前位置
# file.tell()  # 返回文件当前位置。
# file.truncate([size])  # 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
# file.write(str)  # 将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence)  # 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

# 3.3 学习对excel及csv文件进行操作
# 使用Python对Excel进行读写操作：https://blog.csdn.net/MajorDong100/article/details/50708365
# 使用Python对Csv文件操作：https://blog.csdn.net/cigo_2018/article/details/80911385


# 三、作业构
# 读取一个文件【文件将在之后给出】，将文件中转换为字典，key值为学习项目，value值为一个负责人列表，并判断字典中是否有负责人负责多个学习项目。

results = {}
value1 = []
#读取文件
f = file('C:\Users\wb.wuweina\Documents\WeChat Files\wwn035161\Files\homework.txt')
# f = open('homework.txt', mode='r', encoding='UTF-8')
lines = f.readlines()
#将文件中转换为字典
for line in lines:
   key = line.split()[0]
   value = [line.split()[1], line.split()[2]]
   value1 += value
   results[key] = value
f.close()
print(results)
print(value1)
#判断字典中是否有负责人负责多个学习项目
if len(set(value1)) == len(value1):
    print("无人负责多个学习项目")
else:
    print("有人负责多个项目")