# import math
#
# radius = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长： %.2f' % perimeter)
# print('面积:  %.2f' % area)
import math

# 输入年份 如果是闰年就输出 true 如果不是则为false
# year = int(input("请输入年份: "))
#
# is_run = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# print(is_run)


# a = 1
# b = 2
# print(not a)
# print(not False)
# print(a is True)
# print(b is not False)

# a = 'hello Word'
# print(len(a)) # 字符串的长度
# print(a.title()) # 字符串首字母大写
# print(a.upper()) # 字符串大写
# print(a.isupper()) # 字符串是不是大写
# print(a.startswith('hello')) # 字符串是不是以 hello 开头的
# print(a.endswith('word')) # 字符串是不是已 word 结尾
#
# str2 = '- \u9a86\u660a'
# print(str2.title()+' '+str2.lower())

# a = 10
# b = 20
#
# print(a+b)
# print(a-b)
# print(a * b)
# print(a / b)
# print(a // b) # a 除以 b 取去掉小数点后的结果
# print(a % b) # a 除以 b 取余数
# print(a ** b) # a 的 b 次方


# a = int(input('a= '))
# b = int(input('b= '))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# a = int(input('a= '))
# b = int(input('b= '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))
# print('%d % d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))

# a = 100
# b = 1000000000000000000
# c = 12.345
# d = 1 + 5j
# e = 'A'
# f = 'hello, world'
# g = True
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

# a = 100
# b = str(a)
# c = 12.345
# d = str(c)
# e = '123'
# f = int(e)
# g = '12.456'
# h = float(g)
# i = False
# j = str(i)
# k = 'hello'
# m = bool(k)
#
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))
# print(g)
# print(type(g))
# print(h)
# print(type(h))
# print(i)
# print(type(i))
# print(j)
# print(type(j))
# print(k)
# print(type(k))
# print(m)
# print(type(m))

# value = float(input("请输入长度: "))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')

# value = int(input('请输入成绩: '))
# if value < 60 :
#     print('不及格')
# elif 80 > value >= 60:
#     print('中等')
# elif value > 80:
#     print('优秀')
# else:
#     print(value)

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))


# from random import randint
# print(randint(1,12))


# sum = 0
# for i in range(1,100):
#     sum += i
#     print(i)

# sum = 0
# for i in range(2,102,2):
#     sum += i
#     print(i)

# result = 1
# n = int(input("n: "))
# for i in range(1,n+1):
#     result *= i
#     print(result)

# print(math.sqrt(2))

# num = int(input('num: '))
# end = int(math.sqrt(num))
# isEnd = True
# for i in range(2,end+1):
#     if i % num == 0:
#         isEnd = False
# if isEnd and num != 1:
#     print('%d 是素数' % num)
# else:
#     print('%d 不是素数' % num)

# x= int(input('x= '))
# y= int(input('y= '))
#
# if y > x :
#     (y,x) = (x,y)
#
# for factor in range(x,1,-1):
#     if x % factor == 0 and y % factor == 0 :
#         print('%d和%d的最大公约数是%d' % (x,y,factor))
#         print('%d和%d的最小公倍数是%d' % (x,y,x*y))
#         break

# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(i+1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*',end='')
#     print()

# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
#     print(sum)

# sum ,num = 0 ,2
# while num <=100:
#     sum += num
#     num += 2
#     print(sum)





