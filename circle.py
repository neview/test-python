# import math
#
# radius = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长： %.2f' % perimeter)
# print('面积:  %.2f' % area)
import math

import json

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


# obj = {'markHashId_L': '83437b2d-6266-4068-956f-9bbebeed19bf', '_clck': 'uvr0fj|1|fzn|0', 'optimal_cdn_domain': 'res.wx.qq.com', 'low_login_enable': '1', 'TOK': '7ca3d13279e8aa46', 'traceid': '7ca3d13279', 'hashkey': '7ca3d132', 'tdoc_uid': '13102699819316947', 'wedoc_openid': 'wozbKqDgAAEwKWsOKszVZ1t4H5nJbtSQ', 'wedoc_sid': '1tNmdow2Mk8uVERjAAhPTwAA', 'wedoc_sids': '13102699819316947&1tNmdow2Mk8uVERjAAhPTwAA', 'wedoc_skey': '13102699819316947&4ab29531fc50a5cabaaa6c667cf7f3e9', 'wedoc_ticket': '13102699819316947&CAESIILBiDL9okJZiDb5Faw8HtzXjApVYLKFcPBu6niVb9TR'}
# with open('cookies.txt', 'w', encoding='utf-8') as f:  # 建议指定编码为utf-8，避免乱码
#     json.dump(obj, f, ensure_ascii=False, indent=4)  # indent=4让内容格式化，更易读

# with open('cookies.txt', "r", encoding="utf-8") as f:
#     # 把JSON字符串还原为字典对象
#     obj = json.load(f)
#     print(obj)

str='https://doc.weixin.qq.com/forms/j/AKUAmwcxAA4AMcALQaMABgCNUiQoqKq9j_fork?page=5&_cef_tabid_=6a343a0013754480a8260a371b5df1c9#/journal-answer/2?journaluuid=5tnb2GLSq3uGsirYomG29gs46phq2PZQUWckzJpXoosh3JENEHhbb8JESezxH7goye'

str1 = str.split('/forms/j/')[1].split('?')[0]
print(str1)

# import http.client
# import json
#
# conn = http.client.HTTPSConnection("doc.weixin.qq.com")
# payload = json.dumps({
#    "form_id": "AKUAmwcxAA4AMcALQaMABgCNUiQoqKq9j_fork",
#    "fetch_journal_list": True,
#    "is_pre_create": False,
#    "is_answer_from_share": False,
#    "is_answer_from_workplace": False,
#    "fetch_submission_type": 1,
#    "is_only_view": True
# })
# headers = {
#    'Cookie': 'low_login_enable=1;TOK=48c789655dd8205f;traceid=48c789655d;hashkey=48c78965;tdoc_uid=13102699819316947;wedoc_openid=wozbKqDgAAEwKWsOKszVZ1t4H5nJbtSQ;wedoc_sid=1tNmdow2Mk8uVERjAAhPTwAA;wedoc_sids=13102699819316947&1tNmdow2Mk8uVERjAAhPTwAA;wedoc_skey=13102699819316947&4ab29531fc50a5cabaaa6c667cf7f3e9;wedoc_ticket=13102699819316947&CAESIGw187P59vfm8r-JCMuAuw5YYgZsOjgQrv8F7JiRmqlU',
#    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#    'Content-Type': 'application/json',
#    'Accept': '*/*',
#    'Host': 'doc.weixin.qq.com',
#    'Connection': 'keep-alive'
# }
# conn.request("POST", "/journal/get_template_combine_info?_prefetch=1", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

import requests


# def call_api_with_recursion(
#         depend_data=None,  # 上一次接口返回的依赖数据，首次为None
#         current_count=1,  # 当前请求次数，首次从1开始
#         max_count=6  # 最大请求次数，固定为6
# ):
#     """
#     递归调用接口，总共请求6次，每次依赖上一次的数据
#     :param depend_data: 上一次接口返回的依赖数据
#     :param current_count: 当前请求次数
#     :param max_count: 最大请求次数
#     :return: 最后一次接口返回的数据（或所有次的结果列表）
#     """
#     # -------------------------- 1. 递归终止条件 --------------------------
#     if current_count > max_count:
#         print(f"已完成{max_count}次接口请求，递归结束")
#         return depend_data  # 返回最后一次的结果，也可返回所有结果列表
#
#     try:
#         # -------------------------- 2. 构造接口请求参数 --------------------------
#         # 根据上一次的依赖数据，构造本次请求参数（示例逻辑，需替换为你的实际参数）
#         request_params = {}
#         if depend_data:
#             # 假设上一次返回的data.id是本次请求的依赖参数
#             request_params["pre_id"] = depend_data.get("data", {}).get("id")
#         else:
#             # 首次请求的默认参数
#             request_params["pre_id"] = "init_id"
#
#         # -------------------------- 3. 调用接口 --------------------------
#         print(f"开始第{current_count}次接口请求，依赖参数：{request_params}")
#         response = requests.post(
#             url="https://your-api-url.com/xxx",  # 替换为你的接口地址
#             json=request_params,
#             timeout=10  # 设置超时，避免阻塞
#         )
#         response.raise_for_status()  # 触发HTTP状态码非200的异常
#         current_data = response.json()
#         print(f"第{current_count}次接口请求成功，返回数据：{current_data}")
#
#         # -------------------------- 4. 递归调用 --------------------------
#         # 将本次返回的data作为下一次的依赖数据，请求次数+1
#         return call_api_with_recursion(
#             depend_data=current_data,
#             current_count=current_count + 1,
#             max_count=max_count
#         )
#
#     except requests.exceptions.RequestException as e:
#         # 捕获接口请求异常（网络错误、超时、HTTP错误等）
#         print(f"第{current_count}次接口请求失败：{str(e)}")
#         # 可选：重试逻辑（如需重试，可减少count或单独处理）
#         # 此处直接终止递归，也可根据需求调整
#         raise  # 抛出异常，让上层处理；也可返回None或错误信息
#
#
# # -------------------------- 调用示例 --------------------------
# if __name__ == "__main__":
#     try:
#         # 启动递归，首次调用无依赖数据，从第1次开始
#         final_result = call_api_with_recursion()
#         print(f"\n6次接口请求完成，最后一次返回结果：{final_result}")
#     except Exception as e:
#         print(f"递归执行失败：{str(e)}")

def is_date_in_range(check_date, start_date_str, end_date_str, date_format="%Y-%m-%d"):
    # 1. 统一转换 check_date 为 datetime 对象
    if isinstance(check_date, int):
        # 如果是时间戳，转 datetime
        check_dt = datetime.fromtimestamp(check_date)
    elif isinstance(check_date, str):
        # 如果是日期字符串，按格式解析
        check_dt = datetime.strptime(check_date, date_format)
    elif isinstance(check_date, datetime):
        # 如果已经是 datetime 对象，直接使用
        check_dt = check_date
    else:
        raise ValueError("check_date 仅支持 datetime/int(时间戳)/str(日期字符串)")

    # 2. 解析起始和结束日期为 datetime 对象
    start_dt = datetime.strptime(start_date_str, date_format)
    end_dt = datetime.strptime(end_date_str, date_format)

    # 3. 判断是否在范围内（包含边界）
    return start_dt <= check_dt <= end_dt