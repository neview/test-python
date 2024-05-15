# 输出斐波那契数列的前20个数
# 1 1 2 3 5 8 13 21 ...
import math

# a = 0
# b = 1
#
# for i in range(20):
#     a,b = b,a+b
#     print(a,end=' ')


# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

# from random import randint
# num = randint(1,100)
#
# while True:
#     useValue = int(input('你猜是多少'))
#     if useValue == num:
#         print('你猜对了')
#         break
#     elif useValue > num:
#         print('大了一点')
#     elif useValue < num:
#         print('小了一点')


# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数
# 如: 153 = 1**3 + 5**3 + 3**3

# for i in range(100,999):
#     print(i)
#     a = i % 10
#     b = i // 10 % 10
#     c = i // 100
#     if i == a ** 3 + b ** 3 + c ** 3:
#         print(i)


# 判断输入的正整数是不是回文数
# 回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

# num = int(input("Enter a number: "))
# temp = num
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp % 10
#     temp //= 10
# if num == num2:
#     print('%d是回文数' % num)
# else:
#     print('%d不是回文数' % num)

# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14


# import math
#
# for num in range(2, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)

# 输出2~99之间的素数

# import math
#
# for num in range(2,99):
#     is_prime = True
#     for factor in range(2,int(math.sqrt(num))+1):
#         print(factor)
#         if num % factor == 0:
#             is_prime = False
#             break


# 输出乘法口诀表(九九表)

# for i in range(1,10):
#     for j in range(1,10):
#         print('%d x %d = %d' % (i,j,i*j),end=' ')
#     print()




# 函数的定义和使用 - 计算组合数C(7,3)

# def facroe(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#
#     return result
# print(facroe(5) // facroe(6) // facroe(7))


# 函数的定义和使用 - 求最大公约数和最小公倍数

# def GCD(x,y):
#     if x > y:
#         (x,y) = y, x
#     for i in range(x,1,-1):
#         if x % i == 0 and y % i == 0:
#             return i
#     return 1
#
#
# def LCM(x,y):
#     return  x * y // GCD(x,y)
#
# print(LCM(15,27))


# Python的内置函数
# - 数学相关: abs / divmod / pow / round / min / max / sum
# - 序列相关: len / range / next / filter / map / sorted / slice / reversed
# - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
# - 数据结构: dict / list / set / tuple
# - 其他函数: all / any / id / input / open / print / type

# def myfilter(mystr):
#     return len(mystr) == 6


# help()
# print(chr(0x9a86))
# print(hex(ord('骆')))
# print(abs(-1.2345))
# print(round(-1.2345))
# print(pow(1.2345, 5))
# fruits = ['orange', 'peach', 'durian', 'watermelon']
# print(fruits[slice(1, 3)])
# fruits2 = list(filter(myfilter, fruits))
# print(fruits)
# print(fruits2)


# Python常用模块
# - 运行时服务相关模块: copy / pickle / sys / ...
# - 数学相关模块: decimal / math / random / ...
# - 字符串处理模块: codecs / re / ...
# - 文件处理相关模块: shutil / gzip / ...
# - 操作系统服务相关模块: datetime / os / time / logging / io / ...
# - 进程和线程相关模块: multiprocessing / threading / queue
# - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
# - Web编程相关模块: cgi / webbrowser
# - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

import time
import shutil
import os

# seconds = time.time()
# print('当前时间戳的秒数',seconds)
# localtime = time.localtime(seconds) # 不穿seconds 默认是当前时间
# print('包含本地时间元组的结构体',localtime)
# print('%d年%d月%d日 %d时%d分%d秒' % (localtime.tm_year,localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min,localtime.tm_sec))
# asctime = time.asctime(localtime)
# print('可读的ASCII字符串格式',asctime)
# strtime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
# print('时间格式',strtime)
# mydate = time.strptime('2018-1-1','%Y-%m-%d')
# print('字符串2018-1-1解析为时间元组mydate，格式为%Y-%m-%d即年-月-日的格式',mydate)

# shutil.copy('main.py','test_page/main2.py')
# print('复制完成')
# # os.system('ls -l') # 列出当前目录下的文件和文件夹列表
# # os.system('dir') # 列出当前目录下的文件和文件夹列表
# os.chdir('test_page')
# os.system('dir')
# os.mkdir('test2')

# 函数的参数
# - 位置参数
# - 可变参数
# - 关键字参数
# - 命名关键字参数

# def f1(a,b=5,c=2):
#     return a + b + c
#
# print(f1(1,2,3))
# print(f1(100,200))
# print(f1(100))
# print(f1(c=3,b=2,a=1))

# 可变参数
# def fib(*n):
#     num = 0
#     for i in n:
#         num += i
#     return num
#
# print(fib(1,2,3,4,5))
# print(fib(1,2,3))
# print(fib())

# 关键字参数

# def but(**obj):
#     if 'name' in obj:
#         print('你的姓名是 %s' % obj['name'])
#     elif 'age' in obj:
#         print('年龄是 %d' % obj['age'])
#     elif 'tel' in obj:
#         print('手机号码是 %s' % obj['tel'])
#     else:
#         print('没有信息')
#
# aa = {'name':'张三','age':18}
# but(**aa)
# but(user=11,age=18,tel=1733345689)
# but(user=11,age2=18,tel=1733345689)


# 作用域问题

# def foo1():
#     a = 5
#
# foo1()
#
# b = 10
#
# def foo2():
#     print(b)
#
# foo2()
#
#
# def foo3():
#     b = 100     # 局部变量
#     print(b)
#
#
# foo3()
# print(b)
#
#
# def foo4():
#     global b
#     b = 200     # 全局变量
#     print(b)
#
#
# foo4()
# print(b)

# 输入学生考试成绩计算平均分

# num = int(input('请输入学生人数'))
#
# nums = [None] * num
# mark = [None] * num
#
# for i in range(len(nums)):
#     nums[i] = input('请输入%d个学生的名字' % (i+1))
#     mark[i] = float(input('请输入%d个学生的成绩' % (i+1)))
#
# total = 0
# for j in range(len(nums)):
#     print('%s %.1f分' % (nums[j], mark[j]))
#     total += mark[j]
# print('平均分',total / len(nums))

# 定义和使用字典

# scores = {'张三':95,'李四':78,'王五':82}
# print(scores['张三'])
# print(scores['李四'])
# for i in scores:
#     print('%s\t--->\t%d' % (i,scores[i]))
# scores['张三'] = 99
# scores['李四'] = 88
# scores.update(冷面=67,烤冷面=67)
# print(scores)
#
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# print(scores.get('武则天',60))
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('张三',100))
# scores.clear()
# print(scores)


# 字典的常用操作

# scores = {'张三':95,'李四':78,'王五':82}
# # print(scores)
# # print(scores.keys())
# # print(scores.values())
# print(scores.items())
#
# # for i in scores.items():
# #     print(i)
# #     print(i[0],i[1])
#
# if 'age' in scores:
#     scores['age'] = 20
# print(scores)
# scores.setdefault('score',60)
# print(scores)
# scores.setdefault('score',100)
# print(scores)
# scores['score'] = 100
# print(scores)

# 生成斐波拉切数列

# num = [1,1]
# for i in range(2,20):
#     num += [num[i-1]+num[i-2]]
# print(num)
# if __name__ == '__main__':

# 找出列表中最大或最小的元素

# def findOut():
#     fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
#     maxNum = minNum = fruits[0]
#     for i in range(len(fruits)):
#         if fruits[i] > maxNum:
#             maxNum = fruits[i]
#         elif fruits[i] < minNum:
#             minNum = fruits[i]
#
#     print('最大值 %s' % maxNum)
#     print('最小值 %s' % minNum)
#
# findOut()

# 定义和使用列表
# - 用下标访问元素
# - 添加元素
# - 删除元素

# def main():
#     fruits = ['grape', '@pple', 'strawberry', 'waxberry']
#     print(fruits)
#     print(fruits[0])
#     print(fruits[-1])
#     print(fruits[-2])
#     fruits[1] = 'aaa'
#     print(fruits)
#     # 添加元素
#     fruits.append('bbb')
#     print(fruits)
#     fruits.insert(0,'banana')
#     print(fruits)
#     # 删除元素
#     del fruits[0]
#     fruits.pop()
#     fruits.pop(0)
#     fruits.insert(1,'apple')
#     fruits.remove('apple')
#     print(fruits)
#
# main()


# 列表常用操作
# - 列表连接
# - 获取长度
# - 遍历列表
# - 列表切片
# - 列表排序
# - 列表反转
# - 查找元素

# def main():
#     fruits = ['aa','bb','cc','dd']
#     fruits +=['ee','ff']
#     print(fruits)
#
#     for i in fruits:
#         print(i.title(),end=' ')
#     print()
#
#     # 列表切片
#     # fruits2 = fruits[1:4]
#     # print('fruits2 - 列表切片 ',fruits2)
#     # fruits3 = fruits[:]
#     # # fruit3 = fruits  # 没有复制列表只创建了新的引用
#     # print('fruits3 ',fruits3)
#     # fruits4 = fruits[-3:-1]
#     # print('fruits4 ',fruits4)
#     # fruits5 = fruits[::2] 隔两个元素取一个
#     fruits5 = fruits[::-1]
#     print(fruits5)

# main()

# 生成列表
# - 用range创建数字列表
# - 生成表达式
# - 生成器

# 生成Fibonacci序列的生成器

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

def main():
    # 用range创建数值列表
    list1 = list(range(1,11))
    print(list1)

    # 生成表达式
    list2 = [x * x for x in range(1,11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)

main()
















































