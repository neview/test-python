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

import math

class Circle(object):

    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

if __name__ == '__main__':
    radius = float(input("Enter radius: "))
    small = Circle(radius)
    big = Circle(radius+3)
    print('围墙的造假为：￥$.1f元' % (big.perimeter * 115))
    print('过道的造假为：￥%.1f元' % ((big.area - small.area) * 65))



































