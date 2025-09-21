# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 14:34
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
from ollama import chat


def stream_print(response):
    """逐字打印函数"""
    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            print(chunk['message']['content'], end='', flush=True)  # flush=True 保证即时打印


user_content = input("Enter your message: ")
messages = [
    {
        'role': 'user',
        'content': user_content,
    },
]

response = chat('deepseek-r1:7b', messages=messages, stream=True)
# 调用逐字打印函数
stream_print(response)
