#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一、今日学习任务
# 【Day 1】
# 1.环境搭建
# anaconda环境配置
# 解释器
# ---------------------------
# python初体验
# print and input
# ---------------------------
# python基础讲解
# python变量特性+命名规则
# 注释方法
# python中“：”作用
# 学会使用dir( )及和help( )
# import使用
# pep8介绍
# ---------------------------
# python数值基本知识
# python中数值类型，int，float，bool，e记法等
# 算数运算符
# 逻辑运算符
# 成员运算符
# 身份运算符
# 运算符优先级
# ---------------------------
# string字符串
# 定义及基本操作（+，*，读取方式）
# 字符串相关方法
# 字符串格式化问题
# ------------------------------------------------------------------------------------
# 【作业】
# 学习代码分享，200-300行要求。
# 作业：要求用户依次输入姓名，性别，年龄，并对用户信息进行输出格式如下：您的姓名是：***，您的性别是：***，您是***年出生的。
# ------------------------------------------------------------------------------------

# 二、自学及实践内容
# 1. print and input
print('hello, my name is wuweina')  # 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字
print(100+200)  # print()也可以打印整数，或者计算结果

name = input("What is your name:")  # input() 函数接受一个标准输入数据，返回为 string 类型
print name

# 2. python基础讲解
"""
（1）python变量特性+命名规则
变量名只能包含字母、数字和下划线；
变量名不能包含空格，但可使用下划线来分隔其中的单词；
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print；
变量名应既简短又具有描述性；
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

(2)注释方法：在Python中，注释用井号（# ）标识。井号后面的内容都会被Python解释器忽略。多行注释用三个单引号或者三个双引号将注释括起来

(3)python中“：”作用
出现在函数定义语句末尾、if for while语句末尾，表示下面的代码块应当缩进，从属于if for while语句
出现在字典定义当中用于分开键和值

(4)dir()和help()
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。 语法：dir([object])
help() 函数用于查看函数或模块用途的详细说明。 语法：help([object])


(5)import使用
import module1[,... moduleN]  # 模块的引入
from modname import name1[, name2[, ... nameN]]  # 从模块中导入一个指定的部分到当前命名空间中
from modname import *  # 把一个模块的所有内容全都导入到当前的命名空间

(6)pep8介绍: https://alvinzhu.xyz/2017/10/07/python-pep-8/
"""

# 3. python数值基本知识
# (1)数值类型：
type(1)  # 整数(int):
type(1.222)  # 浮点数(float): 即小数
type("test")  # 字符串(string): 以单引号'或双引号"括起来的任意文本  转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
type(True)  # 布尔值(bool): True、False，布尔值可以用and、or和not运算
# 空值: Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# (2)运算符及优先级比较: http://www.runoob.com/python3/python3-basic-operators.html#ysf1 (菜鸟教程)
# 【算数运算符、比较运算符、赋值运算符、逻辑运算符、位运算符、成员运算符、身份运算符】

# 算术运算符
a = 22
b = 12
c = 0
print(a + b, a - b, a * b, a / b, a % b, a ** b, a // b)

# 逻辑运算符
a1 = 10
b1 = 20
if (a1 and b1):  # 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
    print("变量a1和b1都为true")
else:
    print("变量a1和b1有一个不为true")

if (a1 or b1):  # 	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
    print("变量a1和b1都为true, 或其中一个变量为 true")
else:
    print("变量a1和b1都不为true")

if not(a1 and b1):  # 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
    print("变量a1和b1都为true, 或其中一个变量为 true")
else:
    print("变量a1和b1都不为true")

# 成员运算符
a2 = 1
b2 = 20
list = [1, 2, 3, 4, 5]

if (a2 in list):  # 如果在指定的序列中找到值返回 True，否则返回 False。
    print("变量a2在列表list中")
else:
    print("变量a2不在列表list中")

if (b2 not in list):  # 如果在指定的序列中没有找到值返回 True，否则返回 False。
    print("变量b2不在列表list中")
else:
    print("变量b2在列表list中")

# 身份运算符
a3 = 20
b3 = 20

if (a3 is b3):  # is 是判断两个标识符是不是引用自一个对象
    print("a3和b3有相同的标识")
else:
    print("a3和b3没有相同的标识")

b3 = 30
if (a3 is not b3):  # is not 是判断两个标识符是不是引用自不同对象
    print("a3和b3没有相同的标识")
else:
    print("a3和b3有相同的标识")

# 优先级比较：位运算符 > 等于运算符 > 赋值运算符 > 身份运算符 > 成员运算符 > 逻辑运算符

# 4.string字符串
type("Hello World!")  # 字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
"""
Python转义字符
\(在行尾时)  续行符
\\	         反斜杠符号
\'	         单引号
\"	         双引号
\e	         转义
\n	         换行
\v	         纵向制表符
\t	         横向制表符
\r	         回车
\f	         换页
"""

# Python字符串运算符
a = "Hello "
b = "Python "
print "a + b 输出结果：", a + b   # + 字符串连接
print "a * 2 输出结果：", a * 2  # * 重复输出字符串
print "a[1] 输出结果：", a[1]  # [] 通过索引获取字符串中字符
print "a[1:4] 输出结果：", a[1:4]  # [:] 截取字符串中的一部分

# Python 字符串格式化
"""
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址
"""

# 三、作业


import datetime
today = datetime.date.today()
print("你好，请输入您的姓名：")
Name = input()
print("请输入您的性别：")
Sex = input()
print("请输入您的年龄：")
Age = input()
Age = int(Age)
Year = today.year - Age
message = "您的姓名是：%s, 您的性别是：%s, 您是 %d年出生的" %(Name, Sex, Year),
print message
