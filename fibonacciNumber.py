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
from fileinput import filename
from linecache import cache
from stat import filemode
from types import MethodType

import requests
from pygame.draw import lines

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
#
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     # # 用range创建数值列表
#     # list1 = list(range(1,11))
#     # print(list1)
#     #
#     # # 生成表达式
#     # list2 = [x * x for x in range(1,11)]
#     # print(list2)
#     # list3 = [m + n for m in 'ABCDEFG' for n in '12345']
#     # print(list3)
#
#     # 生成器
#     gen = (m+n for m in 'ABCDEFG' for n in '12345')
#     print(gen)
#     for elem in gen:
#         print(elem,end=' ')
#     print()
#     gen = fib(20)
#     print(gen)
#     for elem in gen:
#         print(elem,end=' ')
#     print()
#
# main()

# # 双色球随机选号程序
# from random import randrange, randint, sample
#
# def random_select():
#     red_balls = [x for x in range(1,34)]
#     selected_balls = []
#     for _ in range(6):
#         index = randrange(len(red_balls))
#         selected_balls.append(red_balls[index])
#         del red_balls[index]
#     selected_balls.sort()
#     selected_balls.append(randint(1,16))
#     return selected_balls
#
# def main():
#     num = int(input('输入几注'))
#     for i in range(num):
#         deplay(random_select())
#
# def deplay(obj):
#     for index,bell in enumerate(obj):
#         if index == len(obj)-1:
#             print('|',end=' ')
#         print('%02d' % bell,end=' ')
#     print()
# main()

# 输入学生考试成绩计算平均分

# import os
# import time
#
#
# def main():
#     str = 'Welcome to 1000 Phone Chengdu Campus      '
#     while True:
#         print(str)
#         time.sleep(0.2)
#         str = str[1:] + str[0:1]
#         # for Windows use os.system('cls') instead
#         # os.system('clear')
#         os.system('cls')
#
#
# if __name__ == '__main__':
#     main()

# 定义和使用集合
#
# def main():
#     set1 = {1,2,3,3,3,2}
#     print(set1)
#     print('length =',len(set1))
#     set2 = set(range(1,10))
#     print(set2)
#     set1.add(4)
#     set1.add(5)
#     set2.update([11,12])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#
#     if 4 in set2:
#         set2.remove(4)
#     print('--',set2)
#
#     for elem in set2:
#         print(elem ** 2,end=' ')
#     print()
#
#     set3 = set((1,2,3,3,2,1))
#     print(set3)
#     print(set3.pop())
#     print(set3)
#
# main()

# 集合的常用操作
# - 交集
# - 并集
# - 差集
# - 子集
# - 超集


# def main():
#     set1 = set(range(1,7))
#     print(set1)
#     set2 = set(range(2,11,2))
#     print(set2)
#     set3 = set(range(1,5))
#     print('交集',set1 & set2)
#     print('并集',set1 | set2)
#     print('差集-即输出存在于set1中但不存在于set2中的元素',set1 - set2)
#     print('对称差集-输出存在于set1或set2中但不同时存在的元素',set1 ^ set2)
#     print('判断set2是否为set1的子集，如果是则输出True，否则输出False',set2 <= set1)
#     print('判断set3是否为set1的子集，如果是则输出True，否则输出False',set3 <= set1)
#     print('判断set1是否为set2的超集，如果是则输出True，否则输出False',set1 >= set2)
#     print('判断set1是否为set3的超集，如果是则输出True，否则输出False',set1 >= set3)
#
# if __name__ == '__main__':
#     main()


# 井字棋游戏
# import os
#
# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
#
#
# def main():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('cls')
#         print_board(curr_board)
#         while counter < 9:
#             move = input('轮到%s走棋，请输入位置： ' % turn)
#             if curr_board[move] == ' ':
#                 counter +=1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('cls')
#             print_board(curr_board)
#         choice = input('在玩一句？(yes|no)')
#         begin = choice == 'yes'
#
# if __name__ == '__main__':
#     main()

# 元组的定义和使用
#
# def main():
#     # 定义元组
#     t = ('张三',38,True,'北京')
#     print(t)
#     # 获取元组中的元素
#     print(t[0])
#     print(t[1])
#     print(t[2])
#     print(t[3])
#     # 遍历元组中的值
#     for member in t:
#         print(member)
#     # 重新给元组赋值
#     # t[0] = '李四'
#     # 变量t重新引用了新的元组 原来的元组被垃圾回收
#     t = ('王五',20,True,'上海')
#     print(t)
#     # 元组和列表的转换
#     person = list(t)
#     print(person)
#     person[0] = '李小龙'
#     person[1] = 25
#     print(person)
#     fruits_list = ['apple','banana','orange']
#     fruits_tuple = tuple(fruits_list)
#     print(fruits_tuple)
#     print(fruits_list[1])
#
# if __name__ == '__main__':
#     main()

# 输出10行的杨辉三角 - 二项式的n次方展开系数
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# ... ... ...


# def main():
#     num = int(input("Enter a number: "))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
#             print(yh[row][col],end='\t')
#         print()
#
# if __name__ == '__main__':
#     main()

# class Test:
#
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)
#
#
# if __name__ == "__main__":
#     main()

# 修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
# 过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
# 输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

# import math
#
# class Circle(object):
#
#     def __init__(self,radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self,radius):
#         self._radius = radius if radius > 0 else 0
#
#     @property
#     def perimeter(self):
#         return 2 * math.pi * self._radius
#
#     @property
#     def area(self):
#         return math.pi * self._radius * self._radius
#
# if __name__ == '__main__':
#     radius = float(input("Enter radius: "))
#     small = Circle(radius)
#     big = Circle(radius+3)
#     print('围墙的造假为：￥$.1f元' % (big.perimeter * 115))
#     print('过道的造假为：￥%.1f元' % ((big.area - small.area) * 65))


# 定义和使用时钟类

# import time
# import os
#
# class Clock(object):
#     # Python中的函数是没有重载的概念的
#     # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
#     # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
#     def __init__(self,**kw):
#         if 'houer' in kw and 'minute' in kw and 'second' in kw:
#             self._houer = kw['houer']
#             self._minute = kw['minute']
#             self._second = kw['second']
#         else:
#             tm = time.localtime(time.time())
#             self._houer =tm.tm_hour
#             self._minute = tm.tm_min
#             self._second = tm.tm_sec
#
#     def run(self):
#         self._second +=1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._houer += 1
#                 if self._houer == 24:
#                     self._houer = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._houer, self._minute, self._second)
#
# clock = Clock()
# while True:
#     os.system('cls')
#     print(clock.show())
#     time.sleep(1)
#     clock.run()

# 面向对象版本的猜数字游戏

# from random import randint
#
# class FibonacciNumber(object):
#     def __init__(self):
#         self._answer = None
#         self._counter = None
#         self._hint = None
#
#     def reset(self):
#         self._answer = randint(1,100)
#         print(self._answer)
#         self._counter = 0
#         self._hint = None
#
#     def jisuan(self,obj):
#         self._counter +=1
#         if self._counter > 3:
#             return False
#         if obj > self._answer:
#             return 'max'
#         elif obj < self._answer:
#             return 'min'
#         elif obj == self._answer:
#             return 'success'
#
#     @property
#     def answer(self):
#         return self._answer
#
#     @property
#     def count(self):
#         return self._counter
#
#
# fibonacciNumber = FibonacciNumber()
# fibonacciNumber.reset()
# while True:
#     num = int(input('num:'))
#     if not fibonacciNumber.jisuan(num):
#         print('over')
#     else:
#         print(fibonacciNumber.jisuan(num))

# 另一种创建类的方式

# def bar(self,name):
#     self._name = name
#
# def foo(self,course_name):
#     print('%s正在学习%s.' % (self._name,course_name))
#
# def main():
#     Student = type('Student',(object,),dict(__init__=bar,study = foo))
#     sud1 = Student('张三')
#     sud1.study('javascript')
#
# if __name__ == '__main__':
#     main()

# 定义和使用学生类

# def _foo():
#     print('test')
#
# class Student(object):
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def study(self,course_name):
#         print('%s正在学习%s.' % (self.name,course_name))
#
#     def watch_av(self):
#         if self.age < 18:
#             print('min')
#         else:
#             print('max')
#
# def main():
#     stu1 = Student('张三',38)
#     stu1.study('javascript')
#     stu1.watch_av()
#     stu2 = Student('王大锤',15)
#     stu2.study('java')
#     stu2.watch_av()
#
# if __name__ == '__main__':
#     main()

# 定义和使用矩形类

# class Rect(object):
#     """矩形类"""
#
#     def __init__(self, width=0, height=0):
#         """初始化方法"""
#         self.__width = width
#         self.__height = height
#
#     def perimeter(self):
#         """计算周长"""
#         return (self.__width + self.__height) * 2
#
#     def area(self):
#         """计算面积"""
#         return self.__width * self.__height
#
#     def __str__(self):
#         """矩形对象的字符串表达式"""
#         return '矩形[%f,%f]' % (self.__width, self.__height)
#
#     def __del__(self):
#         """析构器"""
#         print('销毁矩形对象')
#
#
# if __name__ == '__main__':
#     rect1 = Rect()
#     print(rect1)
#     print(rect1.perimeter())
#     print(rect1.area())
#     rect2 = Rect(3.5, 4.5)
#     print(rect2)
#     print(rect2.perimeter())
#     print(rect2.area())

# 多重继承
# - 菱形继承(钻石继承)
# - C3算法(替代DFS的算法)

# class A(object):
#
#     def foo(self):
#         print('foo of A')
#
# class B(A):
#     pass
#
# class C(A):
#     def foo(self):
#         print('foo fo c')
#
# class D(B,C):
#     pass
#
# class E(D):
#
#     def foo(self):
#         print('foo fo d')
#         super().foo()
#         super(B,self).foo()
#         print('-----')
#         super(C,self).foo()
#
# if __name__ == '__main__':
#     d = D()
#     d.foo()
#     e = E()
#     e.foo()

# 对象之间的关联关系

# from math import sqrt
#
#
# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def move_to(self, x, y):
#         self._x = x
#         self._y = y
#
#     def move_by(self, dx, dy):
#         self._x += dx
#         self._y += dy
#
#     def distance_to(self, other):
#         dx = self._x - other._x
#         dy = self._y - other._y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self._x), str(self._y))
#
#
# class Line(object):
#
#     def __init__(self, start=Point(0, 0), end=Point(0, 0)):
#         self._start = start
#         self._end = end
#
#     @property
#     def start(self):
#         return self._start
#
#     @start.setter
#     def start(self, start):
#         self._start = start
#
#     @property
#     def end(self):
#         return self.end
#
#     @end.setter
#     def end(self, end):
#         self._end = end
#
#     @property
#     def length(self):
#         return self._start.distance_to(self._end)
#
#
# if __name__ == '__main__':
#     p1 = Point(3, 5)
#     print(p1)
#     p2 = Point(-2, -1.5)
#     print(p2)
#     line = Line(p1, p2)
#     print(line.length)
#     line.start.move_to(2, 1)
#     line.end = Point(1, 2)
#     print(line.length)

# 属性的使用
# - 访问器/修改器/删除器
# - 使用__slots__对属性加以限制

# class Car(object):
#
#     __slots__ = ('_brand','_max_speed')
#
#     def __init__(self,brand,max_speed):
#         self._brand = brand
#         self._max_speed = max_speed
#
#     @property
#     def brand(self):
#         return self._brand
#
#     @brand.setter
#     def brand(self,brand):
#         self._brand = brand
#
#     @brand.deleter
#     def brand(self):
#         del self._brand
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#     @max_speed.setter
#     def max_speed(self,max_speed):
#         if max_speed < 0:
#             raise ValueError('Invalid max speed for car')
#         self._max_speed = max_speed
#
#     def __str__(self):
#         return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)
#
# car = Car('QQ',120)
# print(car)
# # ValueError
# # car.max_speed = -100
# car.max_speed = 320
# car.brand = 'Bemz'
# # 使用 slots 属性限制后下面的代码将产生异常
# # car.current_speed = 80
# print(car)
# # 如果提供了删除器可以执行下面的代码
# # del car.brand
# print(Car.brand)
# print(Car.brand.fget)
# print(Car.brand.fset)
# print(Car.brand.fdel)
# # 通过上面的代码帮助学生理解之前提到的包装器的概念
# # Python中有很多类似的语法糖后面还会出现这样的东西


# 属性的使用
# - 使用已有方法定义访问器/修改器/删除器

# class Car(object):
#
#     def __init__(self, brand, max_speed):
#         self.set_brand(brand)
#         self.set_max_speed(max_speed)
#
#     def get_brand(self):
#         return self._brand
#
#     def set_brand(self, brand):
#         self._brand = brand
#
#     def get_max_speed(self):
#         return self._max_speed
#
#     def set_max_speed(self, max_speed):
#         if max_speed < 0:
#             raise ValueError('Invalid max speed for car')
#         self._max_speed = max_speed
#
#     def __str__(self):
#         return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)
#
#     # 用已有的修改器和访问器定义属性
#     brand = property(get_brand, set_brand)
#     max_speed = property(get_max_speed, set_max_speed)
#
#
# car = Car('QQ', 120)
# print(car)
# # ValueError
# # car.max_speed = -100
# car.max_speed = 320
# car.brand = "Benz"
# print(car)
# print(Car.brand)
# print(Car.brand.fget)
# print(Car.brand.fset)
# print(car.brand)

# 对象之间的依赖关系和运算符重载

# class Car(object):
#     def __init__(self,brand,max_speed):
#         self._brand=brand
#         self._max_speed=max_speed
#         self._current_speed=0
#
#     @property
#     def brand(self):
#         return self._brand
#
#     def accelerate(self,delta):
#         self._current_speed+=delta
#         if self._current_speed>self._max_speed:
#             self._current_speed = self._max_speed
#
#     def brake(self):
#         self._current_speed=0
#
#     def __str__(self):
#         return '%s当前时速%d' % (self._brand, self._current_speed)
#
# class Student(object):
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     # 学生和车之间存在依赖关系 - 学生使用了汽车
#     def drive(self,car):
#         print('%s驾驶着%s欢快的行驶在去西天的路上' % (self._name, car._brand))
#         car.accelerate(30)
#         print(car)
#         car.accelerate(50)
#         print(car)
#         car.accelerate(50)
#         print(car)
#
#     def study(self,course_name):
#         print('%s正在学习%s.' % (self._name, course_name))
#
#     def watch_av(self):
#         if self._age < 18:
#             print('%s只能观看《熊出没》.' % self._name)
#         else:
#             print('%s正在观看岛国爱情动作片.' % self._name)
#
#     # 重载大于(>)运算符
#     def __gt__(self,other):
#         return self._age > other._age
#
#     #重载小于(<)运算符
#     def __lt__(self,other):
#         return self._age < other._age
#
# if __name__ == '__main__':
#     stu1 = Student('骆昊', 38)
#     stu1.study('Python程序设计')
#     stu1.watch_av()
#     stu2 = Student('王大锤', 15)
#     stu2.study('思想品德')
#     stu2.watch_av()
#     car = Car('QQ', 120)
#     stu2.drive(car)
#     print(stu1 > stu2)
#     print(stu1 < stu2)

# 抽象类 / 方法重写 / 多态
# 实现一个工资结算系统 公司有三种类型的员工
# - 部门经理固定月薪12000元/月
# - 程序员按本月工作小时数每小时100元
# - 销售员1500元/月的底薪加上本月销售额5%的提成
# 输入员工的信息 输出每位员工的月薪信息

# from abc import ABCMeta, abstractmethod
#
# class Employee(object,metaclass=ABCMeta):
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @abstractmethod
#     def get_salary(self):
#         pass
#
# class Manager(Employee):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def get_salary(self):
#         return 12000
#
# class Programmer(Employee):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def set_working_hour(self,working_hour):
#         self.working_hour = working_hour
#
#     def get_salary(self):
#         return 100 * self.working_hour
#
# class Salesman(Employee):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def set_sales(self,sales):
#         self.sales = sales
#
#     def get_salary(self):
#         return 1500+ self.sales * 0.05
#
# if __name__ == '__main__':
#     emps = [Manager('张三'),Programmer('李四'),Salesman('王五')]
#     for emp in emps:
#         if isinstance(emp, Programmer):
#             working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
#             emp.set_working_hour(working_hour)
#         elif isinstance(emp, Salesman):
#             sales = float(input('请输入%s本月销售额: ' % emp.name))
#             emp.set_sales(sales)
#         print('%s本月月薪为: ￥%.2f元' % (emp.name, emp.get_salary()))

# 多重继承
# - 通过多重继承可以给一个类的对象具备多方面的能力
# - 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

# class Father(object):
#     def __init__(self,name):
#         self._name = name
#
#     def gamble(self):
#         print('%s在打麻将' % self._name)
#
#     def eat(self):
#         print('%s在大吃大喝' % self._name)
#
# class Monk(object):
#     def __init__(self,name):
#         self._name = name
#
#     def eat(self):
#         print('%s在吃斋.' % self._name)
#
#     def chant(self):
#         print('%s在念经.' % self._name)
#
# class Musician(object):
#
#     def __init__(self, name):
#         self._name = name
#
#     def eat(self):
#         print('%s在细嚼慢咽.' % self._name)
#
#     def play_piano(self):
#         print('%s在弹钢琴.' % self._name)
#
# class Son(Father, Monk, Musician):
#
#     def __init__(self, name):
#         Father.__init__(self, name)
#         Monk.__init__(self, name)
#         Musician.__init__(self, name)
#
#
# son = Son('王大锤')
# son.gamble()
# # 调用继承自Father的eat方法
# son.eat()
# son.chant()
# son.play_piano()

# from abc import ABCMeta, abstractmethod
#
# class Pet(object, metaclass=ABCMeta):
#     def __int__(self,nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         pass
#
# class Dog(Pet):
#     def make_voice(self):
#         print("I am a Dog")
#
# class  Cat(Pet):
#     def make_voice(self):
#         print("I am a Cat")
#
# def main():
#     pets = [Dog('旺财'), Cat('凯迪'),Dog('大黄')]
#     for pet in pets:
#         pet.make_voice()
#
# if __name__ == '__main__':
#     main()

# 运算符重载 - 自定义分数类
#
# from math import gcd
#
# class Rational(object):
#     def __init__(self, num, den=1):
#         if den == 0:
#             raise ValueError('分母不能为0')
#         self._num = num
#         self._den = den
#         self.normalize()
#
#     def simplify(self):
#         x = abs(self._num)
#         y = abs(self._den)
#         factor = gcd(x, y)
#         if factor > 1:
#             self._den //= factor
#             self._num //= factor
#         return self
#
#     def normalize(self):
#         if self._den < 0:
#             self._den = -self._den
#             self._num = -self._num
#         return self
#
#     def __add__(self, other):
#         new_num = self._num * other._den + other._num * self._den
#         new_den = self._den * other._den
#         return Rational(new_num, new_den).simplify().normalize()
#
#     def __sub__(self, other):
#         new_num = self._num * other._den - other._num * self._den
#         new_den = self._den * other._den
#         return Rational(new_num, new_den).simplify().normalize()
#
#     def __mul__(self, other):
#         new_num = self._num * other._num
#         new_den = self._den * other._den
#         return Rational(new_num, new_den).simplify().normalize()
#
#     def __truediv__(self, other):
#         new_num = self._num * other._den
#         new_den = self._den * other._num
#         return Rational(new_num, new_den).simplify().normalize()
#
#     def __str__(self):
#         if self._num == 0:
#             return '0'
#         elif self._den == 1:
#             return str(self._num)
#         else:
#             return '(%d/%d)' % (self._num, self._den)
#
# if __name__ == '__main__':
#     r1 = Rational(2, 3)
#     print(r1)
#     r2 = Rational(6, -8)
#     print(r2)
#     print(r2.simplify())
#     print('%s + %s = %s' % (r1, r2, r1 + r2))
#     print('%s - %s = %s' % (r1, r2, r1 - r2))
#     print('%s * %s = %s' % (r1, r2, r1 * r2))
#     print('%s / %s = %s' % (r1, r2, r1 / r2))

# 游戏

# from enum import Enum, unique
# from math import sqrt
# from random import randint
#
# import pygame
#
#
# @unique
# class Color(Enum):
#     """颜色"""
#
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (242, 242, 242)
#
#     @staticmethod
#     def random_color():
#         """获得随机颜色"""
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         return (r, g, b)
#
#
# class Ball(object):
#     """球"""
#
#     def __init__(self, x, y, radius, sx, sy, color=Color.RED):
#         """初始化方法"""
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move(self, screen):
#         """移动"""
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy
#
#     def eat(self, other):
#         """吃其他球"""
#         if self.alive and other.alive and self != other:
#             dx, dy = self.x - other.x, self.y - other.y
#             distance = sqrt(dx ** 2 + dy ** 2)
#             if distance < self.radius + other.radius \
#                     and self.radius > other.radius:
#                 other.alive = False
#                	self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self, screen):
#         """在窗口上绘制球"""
#         pygame.draw.circle(screen, self.color,
#                            (self.x, self.y), self.radius, 0)
#
#
# def main():
#     # 定义用来装所有球的容器
#     balls = []
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     print(screen.get_width())
#     print(screen.get_height())
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     # 定义变量来表示小球在屏幕上的位置
#     x, y = 50, 50
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 x, y = event.pos
#                 radius = randint(10, 100)
#                 sx, sy = randint(-10, 10), randint(-10, 10)
#                 color = Color.random_color()
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 balls.append(ball)
#         screen.fill((255, 255, 255))
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#         pygame.display.flip()
#         # 每隔50毫秒就改变小球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             for other in balls:
#                 ball.eat(other)
#
#
# if __name__ == '__main__':
#     main()

# 事件交互
# import tkinter
# import tkinter.messagebox
#
#
# def main():
#     flag = True
#
#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello, world!')\
#             if flag else ('blue', 'Goodbye, world!')
#         label.config(text=msg, fg=color)
#
#     # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
#             top.quit()
#
#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标题
#     top.title('小游戏')
#     # 创建标签对象
#     label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# 画布视图
# import tkinter
#
#
# def mouse_evt_handler(evt=None):
#     row = round((evt.y - 20) / 40)
#     col = round((evt.x - 20) / 40)
#     pos_x = 40 * col
#     pos_y = 40 * row
#     canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')
#
#
# top = tkinter.Tk()
# # 设置窗口尺寸
# top.geometry('620x620')
# # 设置窗口标题
# top.title('五子棋')
# # 设置窗口大小不可改变
# top.resizable(False, False)
# # 设置窗口置顶
# top.wm_attributes('-topmost', 1)
# canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
# canvas.bind('<Button-1>', mouse_evt_handler)
# canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
# for index in range(15):
#     canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
#     canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
# canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
# canvas.pack()
# tkinter.mainloop()

# 窗口制作动画


# import tkinter
# import time
#
#
# # 播放动画效果的函数
# def play_animation():
#     canvas.move(oval, 2, 2)
#     canvas.update()
#     top.after(50, play_animation)
#
#
# x = 10
# y = 10
# top = tkinter.Tk()
# top.geometry('600x600')
# top.title('动画效果')
# top.resizable(False, False)
# top.wm_attributes('-topmost', 1)
# canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
# canvas.create_rectangle(0, 0, 600, 600, fill='gray')
# oval = canvas.create_oval(10, 10, 60, 60, fill='red')
# canvas.pack()
# top.update()
# play_animation()
# tkinter.mainloop()

 # csv文件

# import csv
#
# filename = 'teacher.csv'
# teachers = [['aaa','18','a--a'],['bbb','19','b--b'],['ccc','20','c--c']]
#
# try:
#     with open(filename,'w') as f:
#         writer = csv.writer(f)
#         for teacher in teachers:
#             writer.writerow([teacher[0],teacher[1],teacher[2]])
# except BaseException as e:
#     print('无法写入',filename)
# else:
#     print('保存数据')


# 判断文件内容是否存在xxx

# filename = 'aa.txt'
# bb = '123123'
# with open(filename) as f:
#     lines = f.readlines()
#     aa = ''
#     for line in lines:
#         aa+=line.strip()
#     if bb in aa:
#         print('存在')

#  try 异常捕获
# input_again = True
#
# while input_again:
#     try:
#         a = int(input('a='))
#         b = int(input('b='))
#         print('%d / %d = %f' % (a, b, a / b))
#     except ValueError:
#         print('数不对')
#     except ZeroDivisionError:
#         print('除数不能为0')

# 异常
# bool = True
#
# while bool:
#     try:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         print('%d / %d = %s' % (a, b, a/b))
#         bool = False
#     except (ValueError,ZeroDivisionError) as msg:
#         print(msg)

# 读取文件
# import time
# import sys
#
# filenme = input('请输入文件名')
# try:
#     with open(filenme) as f:
#         lines = f.readlines()
# except FileNotFoundError as msg:
#     print('无法打开文件:',filenme)
#     print(msg)
# except UnicodeDecodeError as msg:
#     print('非文本文件无法解码')
#     sys.exit()
# else:
#     for line in lines:
#         print(line.rstrip())
#         time.sleep(0.5)
# finally:
#     print('成功失败都执行')


# 多种方式读取文件
import time

from pygame.examples.go_over_there import target_position

# filename = 'aa.txt'
# def main():
#     # with open(filename, 'r',encoding='utf-8') as f:
#     #     print(f.read())
#
#     # with open(filename, 'r') as f:
#     #     for line in f:
#     #         print(line)
#
#     with open(filename) as f:
#         lines = f.readlines()
#     print(lines)
#
# main()

# 写入文件
# from math import sqrt
#
# def is_prime(n):
#     for factor in range(2, int(sqrt(n))+1):
#         if n % factor == 0:
#             return False
#     return True
#
# with open('aa.txt','w') as f:
#     for num in range(2,100):
#         if is_prime(num):
#             f.write(str(num)+'\n')
# print('写入完成')

# 读写二进制文件

# import base64
# with open('aa.jpg', 'rb') as f:
#     data = f.read()
#     print('字节数:',len(data))
#     print(base64.b64encode(data))
#
# with open('bb.jpg', 'wb') as f:
#     f.write(data)
#
# print('写入完成')

# 处理json数据
# import json
# # import csv2
#
# json_str = '{"name":"xx","age":"38","title":"嘿嘿"}'
# result = json.loads(json_str)
# print(result)
# print(type(result))
# print(result['name'])
# print(result['age'])

# 转义字符
# print('My brother\'s name is \'007\'')

# 原始字符
# print(r'My brother\'s name is \'007\'')

# str = 'hello123world'
# print('he' in str)
# print('her' in str)

# 字符串是否只包含字母
str = 'hello123world'
# print(str.isalpha())

# 字符串是否只包含字母和数字
# print(str.isalnum())

# 字符串是否只包含数字
# print(str.isdecimal())

# sentence = 'You go your way I will go mine'
# words_list = sentence.split()
# print(words_list)

# print(range(10 // 2))
# print(range(10 -1 , 10 // 2,-1))

# import asyncio
# import threading
#
# async def hello():
#     print('%s: hello, world!' % threading.current_thread())
#     await asyncio.sleep(2)
#     print('%s: goodbye, world!' % threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# def log(func):
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def now():
#     print('2024-6-1')
#
# now()

# import types
#
# def aa():
#     print('aa')
#
# print(type(aa))
# print(type(aa) == types.FunctionType)


# class Aa():
#     def __init__(self):
#         self.a = 1
#
# obj = Aa()
# print(hasattr(obj, 'x'))

class Aa(object):
    def __init__(self):
        self.age = 1

# def set_age2(self,*age):
#     self.age = age
#     print('set_age2',self.age)
# s = Aa()
# s.set_age = MethodType(set_age2,s)
# print(s.set_age(1))
# print(s.age)

# import pdb
# a = 0
# print(1)
# a = 2
# pdb.set_trace()
# print(a)

# class Dict():
#     def __init__(self,**kw):
#         super().__init__(**kw)
#
#     def __getstate__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(f'key {key} not found in Dirt')
#
#     def __setstate__(self,key,value):
#         self[key] = value
#
#     def __iter__(self):
#         return iter(self.data)
#
#
# import unittest
#
#
# class TestDict(unittest.TestCase):
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
# if __name__ == '__main__':
#     unittest.main()


# f = open('aa.txt', 'r')
# print(f.read())
# f.close()

import os
# print(os.name)
# print(os.environ)
# print(os.environ.get('ALLUSERSPROFILE'))

# print(os.path.abspath('.')) # 当前目录的路径
# print(os.path.join(r'\python\/test','text-10'))
# os.mkdir(r'\python\test\text-10')

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

import pickle
# d = dict(name='AA',age=20,score=88)
# f = open('aa.txt','wb')
# pickle.dump(d,f)
# f.close()

# f = open('aa.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)


# import os
# import multiprocessing as Process
#
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process start.')
#     p.start()
#     print('Child process end.')
#     p.join()

# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# import time, threading
#
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()



# import threading
# import requests
#
# def make_request(url):
#     response = requests.get(url)
#     print(f"Response from {url}: {response.status_code}")
#
# # 要请求的接口列表
# urls = [
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/3"
# ]
#
# # 创建并启动线程
# threads = []
# for url in urls:
#     thread = threading.Thread(target=make_request, args=(url,))
#     threads.append(thread)
#     thread.start()
#
# # 等待所有线程完成
# for thread in threads:
#     thread.join()












































