import json
from datetime import datetime
import ast

import pyperclip


# def deduplicate_and_sort_by_field(arr, field="A", keep_last=True, reverse=False):
#     """
#     根据指定字段去重并排序数组（字典数组）
#     :param arr: 原始数组（元素为字典）
#     :param field: 去重/排序的字段（默认"A"）
#     :param keep_last: 去重时保留最后一次出现的项（True）/首次出现的项（False）
#     :param reverse: 排序是否降序（True=降序，False=升序）
#     :return: 去重+排序后的新数组
#     """
#     # 步骤1：去重 - 利用字典键唯一特性
#     unique_dict = {}
#     for item in arr:
#         # 确保字段存在，避免KeyError
#         if field not in item:
#             raise ValueError(f"数组项缺少字段：{field}")
#
#         key = item[field]
#         # 保留末次出现：直接覆盖；保留首次出现：仅当键不存在时赋值
#         if keep_last or key not in unique_dict:
#             unique_dict[key] = item
#
#     # 步骤2：提取去重后的列表，并按A字段排序
#     # sorted的key参数指定排序依据，reverse控制升降序
#     sorted_list = sorted(
#         unique_dict.values(),
#         key=lambda x: x[field],  # 按A字段的值排序
#         reverse=reverse
#     )
#
#     return sorted_list
#
# with open('list.txt', "r", encoding="utf-8") as f:
#     # 把JSON字符串还原为字典对象
#     text_content = f.read().strip()
#     # for item in ast.literal_eval(text_content):
#     #     print(item)
#     result1 = deduplicate_and_sort_by_field(ast.literal_eval(text_content), field="createtime")
#     # print(ast.literal_eval(text_content))
#     for item in result1:
#         print(datetime.fromtimestamp(item['createtime']))
#     # print("去重（保留末次）+ 升序：", result1)

# import pyperclip
#
#
# def format_data_and_copy(data, type=1, remove_duplicate=True, for_mubu=False):
#     """
#     格式化数据并复制到剪贴板（支持普通格式/幕布格式，控制是否带序号）
#     :param data: 原始数据数组
#     :param type: 格式类型 1-带连续序号（默认） 2-不带序号（仅普通格式生效）
#     :param remove_duplicate: 是否去除list中的重复项（默认True）
#     :param for_mubu: 是否适配幕布格式（默认False，True时强制无序号+清理标题符号）
#     :return: 格式化后的文本
#     """
#
#     # 工具函数1：去除原有序号，保留纯文本内容
#     def remove_original_number(text):
#         if '、' in text:
#             parts = text.split('、', 1)  # 仅分割第一个「、」
#             if parts[0].strip().isdigit():
#                 return parts[1].strip()
#         return text.strip()
#
#     # 工具函数2：清理幕布标题的特殊符号（【】）
#     def clean_mubu_title(title):
#         return title.replace('【', '').replace('】', '').strip()
#
#     # 校验参数合法性
#     if type not in [1, 2]:
#         print("⚠️ type参数仅支持1（带序号）或2（不带序号），已默认使用type=1")
#         type = 1
#
#     # 幕布模式下强制type=2（无序号）
#     if for_mubu:
#         type = 2
#
#     formatted_text = ""
#     for item in data:
#         # 拼接title（幕布模式清理特殊符号）
#         title = item.get('title', '')
#         if not title:
#             continue
#         if for_mubu:
#             title = clean_mubu_title(title)
#         formatted_text += f"{title}\n"
#
#         # 处理list数据
#         list_items = item.get('list', [])
#         if not list_items:
#             continue
#
#         # 步骤1：去重 + 剥离原有序号
#         if remove_duplicate:
#             seen = set()
#             unique_list = []
#             for li in list_items:
#                 pure_text = remove_original_number(li)
#                 if pure_text not in seen:
#                     seen.add(pure_text)
#                     unique_list.append(pure_text)
#             list_items = unique_list
#         else:
#             list_items = [remove_original_number(li) for li in list_items]
#
#         # 步骤2：根据type/幕布模式生成列表项
#         if type == 1 and not for_mubu:
#             # 普通模式+带序号
#             for idx, pure_text in enumerate(list_items, 1):
#                 formatted_text += f"    {idx}、{pure_text}\n"
#         else:
#             # 普通模式无序号 / 幕布模式（均无序号）
#             for pure_text in list_items:
#                 formatted_text += f"    {pure_text}\n"
#
#         # 每个title后加空行分隔
#         formatted_text += "\n"
#
#     # 去除末尾多余空行
#     formatted_text = formatted_text.strip()
#
#     # 复制到剪贴板
#     try:
#         pyperclip.copy(formatted_text)
#         if for_mubu:
#             print(f"✅ 数据已适配幕布格式并复制到剪贴板！")
#         else:
#             print(f"✅ 数据已按type={type}格式化为并复制到剪贴板！")
#         print("------------------------ 格式化结果预览 ------------------------")
#         print(formatted_text)
#     except Exception as e:
#         print(f"❌ 复制到剪贴板失败：{str(e)}")
#         print("------------------------ 格式化结果 ------------------------")
#         print(formatted_text)
#
#     return formatted_text
#
#
# # 执行格式化并复制
# if __name__ == "__main__":
#     with open('test2.txt', "r", encoding="utf-8") as f:
#         # 把JSON字符串还原为字典对象
#         text_content = f.read().strip()
#         # format_data_and_copy(ast.literal_eval(text_content), type=1)
#         format_data_and_copy(ast.literal_eval(text_content), for_mubu=True)


# # 判断日期是否在范围内
# def is_date_in_range(check_date, start_date_str, end_date_str, date_format="%Y-%m-%d"):
#     # 1. 统一转换 check_date 为 datetime 对象
#     if isinstance(check_date, int):
#         # 如果是时间戳，转 datetime
#         check_dt = datetime.fromtimestamp(check_date)
#     elif isinstance(check_date, str):
#         # 如果是日期字符串，按格式解析
#         check_dt = datetime.strptime(check_date, date_format)
#     elif isinstance(check_date, datetime):
#         # 如果已经是 datetime 对象，直接使用
#         check_dt = check_date
#     else:
#         raise ValueError("check_date 仅支持 datetime/int(时间戳)/str(日期字符串)")
#
#     # 2. 解析起始和结束日期为 datetime 对象
#     start_dt = datetime.strptime(start_date_str, date_format)
#     end_dt = datetime.strptime(end_date_str, date_format)
#
#     # 3. 判断是否在范围内（包含边界）
#     return start_dt <= check_dt <= end_dt
#
# if __name__ == "__main__":
#     with open('list.txt', "r", encoding="utf-8") as f:
#         # 把JSON字符串还原为字典对象
#         text_content = f.read().strip()
#         strTime = "2025-12-29"
#         endTime = "2025-12-31"
#         # format_data_and_copy(ast.literal_eval(text_content), type=1)
#         list = ast.literal_eval(text_content)
#         for item in list:
#             if is_date_in_range(item['createtime'], strTime, endTime):
#                 print('YES')
#             else:
#                 print('NO')

def format_data_and_copy(data, type=1, remove_duplicate=False):
    """
    格式化数据并复制到剪贴板（支持控制是否带序号）
    :param data: 原始数据数组
    :param type: 格式类型 1-带连续序号（默认） 2-不带序号
    :param remove_duplicate: 是否去除list中的重复项（默认True）
    :return: 格式化后的文本
    """

    # 工具函数：去除原有序号，保留纯文本内容
    def remove_original_number(text):
        if '、' in text:
            parts = text.split('、', 1)  # 仅分割第一个「、」
            if parts[0].strip().isdigit():
                return parts[1].strip()
        return text.strip()

    # 校验type参数合法性
    if type not in [1, 2]:
        print("⚠️ type参数仅支持1（带序号）或2（不带序号），已默认使用type=1")
        type = 1

    formatted_text = ""
    for item in data:
        # 拼接title
        title = item.get('title', '')
        if not title:
            continue
        formatted_text += f"{title}\n"

        # 处理list数据
        list_items = item.get('list', [])
        if not list_items:
            continue

        # 步骤1：去重 + 剥离原有序号
        if remove_duplicate:
            seen = set()
            unique_list = []
            for li in list_items:
                pure_text = remove_original_number(li)
                if pure_text not in seen:
                    seen.add(pure_text)
                    unique_list.append(pure_text)
            list_items = unique_list
        else:
            list_items = [remove_original_number(li) for li in list_items]

        # 步骤2：根据type生成不同格式的列表项
        if type == 1:
            # type=1：带连续序号（1、2、3...）
            for idx, pure_text in enumerate(list_items, 1):
                formatted_text += f"    {idx}、{pure_text}\n"
        elif type == 2:
            # type=2：不带序号，仅纯文本
            for pure_text in list_items:
                formatted_text += f"    {pure_text}\n"

        # 每个title后加空行分隔
        formatted_text += "\n"

    # 去除末尾多余空行
    formatted_text = formatted_text.strip()

    # 复制到剪贴板
    try:
        pyperclip.copy(formatted_text)
        print(f"✅ 数据已格式化为并复制到剪贴板！")
        print("------------------------ 格式化结果预览 ------------------------")
        print(formatted_text)
    except Exception as e:
        print(f"❌ 复制到剪贴板失败：{str(e)}")
        print("------------------------ 格式化结果 ------------------------")
        print(formatted_text)

    return formatted_text

if __name__ == "__main__":
    list = [{'title': '【芒果电影商家】', 'list': ['1、新增客服链接跳转中间页', '2、配置微信后台的业务域名功能', '3、编写企业微信与H5动态跳转的逻辑', '1、配置微信后台的业务域名功能', '2、修改测试后的问题', '3、测试webview页面新增自动刷新功能', '1、排查开发版本提现信息页面不显示的问题','2、优化注销提示页面的跳转逻辑', '3、优化注销确认页面的逻辑处理', '4、修改测试后的问题', '5、优化注销确认页面的价格处理逻辑']}, {'title': '【芒果总后台】', 'list': ['1、优化供应商客服设置功能']}]
    format_data_and_copy(list, type=1)
