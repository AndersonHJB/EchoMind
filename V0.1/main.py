# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 14:34
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
from ollama import chat


# def cot_status(cot=False):
#     """Chain of Thought"""


def stream_print(response, show_think=False):
    """逐字打印函数
    :param response: ollama 返回的流式结果
    :param show_think: 是否显示思维链
    """
    think_count = 0
    for chunk in response:
        if ('message' in chunk) and ('content' in chunk['message']):
            msg = chunk['message']['content']

            if 'think>' in msg:
                think_count += 1
                if show_think:  # 如果允许展示思维链，直接打印
                    print(msg, end='', flush=True)
            else:
                if show_think:
                    # 直接打印所有输出（包括思维链）
                    print(msg, end='', flush=True)
                else:
                    # 不展示思维链时，只打印第2次think之后的内容（即最终回答）
                    if think_count >= 2:
                        print(msg, end='', flush=True)


user_content = input("Enter your message: ")
messages = [
    {
        'role': 'user',
        'content': user_content,
    },
]

response = chat('deepseek-r1:7b', messages=messages, stream=True)
# 调用逐字打印函数
stream_print(response, show_think=True)
