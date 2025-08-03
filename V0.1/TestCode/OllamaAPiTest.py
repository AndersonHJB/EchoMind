# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 14:34
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
from ollama import chat
import time


def typewriter_print(response, delay=0.05):
    """拟人化逐字打字机效果打印"""
    think_count = 0
    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            # print(chunk['message']['content'], end='', flush=True)  # flush=True 保证即时打印
            # print(chunk['message']['content'])
            # for char in chunk['message']['content']:
            #     print(char, end='', flush=True)
            #     time.sleep(delay)  # 控制打字速度
            if think_count == 2:
                print(chunk['message']['content'])
            # elif 'think>' in chunk['message']['content']:
            # elif chunk['message']['content'] == '<think>' or chunk['message']['content'] == '</think>':
            elif chunk['message']['content'] in ('<think>', '</think>'):
            # elif 'think>' in str(chunk['message']['content']):
                think_count += 1
                # if think_count == think_target:
                #     print("思考中...", end='', flush=True)
                #     time.sleep(1)
    print()  # 打印完毕后换行


user_content = input("Enter your message: ")

messages = [
    {
        'role': 'user',
        'content': user_content,
    },
]

# 使用 stream=True 开启流式输出
response = chat('deepseek-r1:7b', messages=messages, stream=True)

# 拟人化逐字打印
typewriter_print(response, delay=0.06)

print("\n--- 完成 ---")
