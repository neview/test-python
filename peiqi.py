# from turtle import *
#
#
# def test():
#     penup()
#     goto(10, 20)
#     pendown()
#     a = 0.4
#     for i in range(120):
#         if 0 < i or 30 < i < 90:
#             a = a + 0.08
#             left(3)
#             forward(a)
#         else:
#             a = a - 0.08
#             left(3)
#             forward(a)
#
#
# test()
# import requests
#
# urlM = "https://supplier.mgmovie.net/v2/api/"
# headers9 = {'user-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImFkbWluX2lkIjo3N30sImlzcyI6Im1hbmdvIiwiaWF0IjoxNzU3OTE1NzA5LCJleHAiOjE3NjA1MDc3MDl9.H_0IG5mfaelDMV7TWFtniBLGZuCHNJ_ItKccLMhUryY'}
# # responseId = requests.get(urlM + "62cbf4622b81b", headers=headers9,json={'app_id': 3082, 'page': 1, 'pageSize': 30}).json()
# # if responseId['code'] == 1:
# #     print(responseId)
# response12 = requests.get(urlM + "62fc9d43dc3a7", headers=headers9, params={"business_id": 3082}).json()
# print(response12)
import sys

import requests

# import base64
# import hashlib
# import warnings
# import requests
#
# file_path = 'aa.jpg'
# try:
#     with open(file_path, 'rb') as file:
#         file_data = file.read()
#         # Base64编码（去除换行符，适配JSON格式）
#         base64_data = base64.b64encode(file_data).decode('utf-8').replace('\n', '')
#         # MD5哈希（用于图片完整性校验）
#         md5_hash = hashlib.md5(file_data).hexdigest()
#         if not base64_data:
#             warnings.warn('文件缺失')
#
#         obj={
#               "msgtype": "image",
#               "image": {
#                 "base64": base64_data,
#                 "md5": md5_hash,
#               },
#             }
#         response13 = requests.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4cbef34d-76fe-42f1-b218-20c89264279c", headers={"Content-Type": "application/json"}, json=obj).json()
#         print(response13['errcode'])
#
#         name = ["陈思佳"]
#         obj2 = {
#             "msgtype": "text",
#             "text": {
#                 "content": ' @' + name[0] + ' 测试saas微信小程序',
#                 "mentioned_list": name,
#             },
#         }
#         response14 = requests.post(
#             "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4cbef34d-76fe-42f1-b218-20c89264279c",
#             json=obj2).json()
#
#         print(response14)
# except Exception as e:
#     print(f"读取文件失败：{e}")
# a = 'xx'
# print('aa')
# sys.exit(400)
# print([a])
from datetime import datetime
import json
obj = json.dumps({
   "form_id": "AKUAmwcxAA4AMcALQaMABgCNf7n21ksIj_fork",
   "fetch_journal_list": True,
   "is_pre_create": False,
   "is_answer_from_share": False,
   "is_answer_from_workplace": False,
   "fetch_submission_type": 1,
   "is_only_view": True
})
cookies ={
    "low_login_enable":"1",
    "markHashId_L":"83437b2d-6266-4068-956f-9bbebeed19bf",
    "_clck":"uvr0fj|1|fzn|0",
    "TOK":"5b032a468d2cbd91",
    "traceid":"5b032a468d",
    "hashkey":"5b032a46",
    "tdoc_uid":"13102699819316947",
    "wedoc_openid":"wozbKqDgAAEwKWsOKszVZ1t4H5nJbtSQ",
    "wedoc_sid":"1tNBeYw2RFouVFhnAAhZWgAA",
    "wedoc_sids":"13102699819316947&1tNBeYw2RFouVFhnAAhZWgAA",
    "wedoc_skey":"13102699819316947&539bb6bbe67b44e59d7e8c65b0021394",
    "wedoc_ticket":"13102699819316947&CAESIOhfFQfmksobMS1Nh5CvEQmH0mdZXr2Wuj2G1kSii9Ja",
    "optimal_cdn_domain":"res.wx.qq.com"
}
headers = {
    'Cookie': 'low_login_enable=1;markHashId_L=83437b2d-6266-4068-956f-9bbebeed19bf;_clck=uvr0fj|1|fzn|0;TOK=5b032a468d2cbd91;traceid=5b032a468d;hashkey=5b032a46;tdoc_uid=13102699819316947;wedoc_openid=wozbKqDgAAEwKWsOKszVZ1t4H5nJbtSQ;wedoc_sid=1tNBeYw2RFouVFhnAAhZWgAA;wedoc_sids=13102699819316947&1tNBeYw2RFouVFhnAAhZWgAA;wedoc_skey=13102699819316947&539bb6bbe67b44e59d7e8c65b0021394;wedoc_ticket=13102699819316947&CAESIOhfFQfmksobMS1Nh5CvEQmH0mdZXr2Wuj2G1kSii9Ja;optimal_cdn_domain=res.wx.qq.com',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': 'doc.weixin.qq.com',
   'Connection': 'keep-alive'
}
response13 = requests.post(
                "https://doc.weixin.qq.com/journal/get_template_combine_info?_prefetch=1",
                headers=headers, data=obj).json()
# for item in response13['body']['entrys']:
#     if item['journalid'] is not None and item['showinfo']['wordings'] is not None:
#         dt_object = datetime.fromtimestamp(item['createtime'])
#         formatted_date = dt_object.strftime("%Y-%m-%d")
#         print(f"{item.get('journalid')}-{formatted_date}-{item.get('showinfo', {}).get('wordings')}")
#     else:
#         print('缺失')

for item in response13['body']['entrys']:

