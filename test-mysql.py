# import mysql.connector
#
# # 连接到 MySQL 数据库
# try:
#     connection = mysql.connector.connect(
#         host="39.100.77.85",       # 数据库主机（比如 127.0.0.1）
#         user="root",            # 数据库用户名
#         password="P4jtDFKzPT7wpfRa", # 数据库密码
#         database="big_event", # 数据库名称
#         port=13306
#     )
#
#     # 检查连接状态
#     if connection.is_connected():
#         print("成功连接！")
#
#         # 创建游标对象
#         cursor = connection.cursor()
#
#         # 执行查询语句
#         query = "SELECT * FROM user;"
#         cursor.execute(query)
#
#         # 获取查询结果
#         results = cursor.fetchall()
#
#         # 打印结果
#         for row in results:
#             print(row)
#
# except mysql.connector.Error as e:
#     print(f"连接失败：{e}")
# finally:
#     # 关闭连接
#     if 'cursor' in locals() and cursor:
#         cursor.close()
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("连接已关闭。")

# import sys
# import requests
# import time
# import json
# import types
# import os
#
# url = "https://fun-api.huanxio.com/h5/addressList"
#
# headers = {
#     "uk-token": "612",
#     "Content-Type": "application/json"
# }
#
# payload = json.dumps({
#     "user_id": 43167405,
#     "current": 1,
#     "type": 0
# })
#
# num = 1
#
#
# def file(obj):
#     # 获取当前文件的目录路径
#     current_dir = os.path.dirname(__file__)
#
#     # 拼接文件路径
#     file_path = os.path.join(current_dir, "result.txt")
#
#     # 创建文件并写入内容
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(obj)
#
#
# while num < 2:
#     num += 1
#     try:
#         response = requests.post(url, headers=headers, data=json.dumps({
#             "user_id": 43167405,
#             "current": 1,
#             "type": 0
#         }))
#         # print("body:",response.request.body)
#         data = types.SimpleNamespace(**response.json())
#         if data.code == 0:
#             print(f"\033[32m{data.result}\033[0m")
#             file(json.dumps(data.result, ensure_ascii=False, indent=4))
#             sys.exit()
#         # else:
#         # print(f"\033[31m{data.message}\033[0m")
#
#     except requests.exceptions.RequestException as e:
#         print(f"\033[31m{e}\033[0m")
#
#     time.sleep(0.2)

import os
import sys

a = 1
b = 2

while a < 5:
    current_dir = os.path.dirname(__file__)

    file_path = os.path.join(current_dir, f"agent：{a}.txt")

    while b < 5:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"id：{b}" + "\n")
        b += 1
    a += 1
    b = 1

sys.exit()