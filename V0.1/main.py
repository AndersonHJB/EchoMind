# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 14:34
# @Author  : AI悦创
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
import time
import random
from ollama import chat
import sys


def thinking_effect(thinking_time=3, interval=0.5):
    """
    在回答前模拟思考效果：点会循环出现（清除旧点再显示新点）
    - thinking_time: 总思考时间
    - interval: 每个点之间的间隔
    """
    start = time.time()
    dots = ["", ".", "..", "..."]
    i = 0
    while time.time() - start < thinking_time:
        sys.stdout.write("\r思考中" + dots[i % 4])  # \r 回到行首覆盖
        sys.stdout.flush()
        time.sleep(interval)
        i += 1
    print("\r" + " " * 20, end="\r")  # 清空这行
    print("思考完成，开始回答：\n")  # 提示进入回答阶段


def typewriter_print(response, base_delay=0.04, var_delay=0.04, punct_delay=0.3):
    """拟人化逐字打字机效果打印"""
    punctuation = "，。！？：；,.!?;:"  # 中英文常用标点

    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            for char in chunk['message']['content']:
                print(char, end='', flush=True)
                # 随机延迟
                time.sleep(base_delay + random.uniform(0, var_delay))
                # 遇到标点额外停顿
                if char in punctuation:
                    time.sleep(punct_delay)
    print()


def stream_print(response):
    """原始即时输出"""
    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            print(chunk['message']['content'], end='', flush=True)
    print()


def print_response(response, mode="normal"):
    """
    统一接口，可选打字效果:
    - normal: 拟人化逐字输出（含思考）
    - fast: 简单逐字输出，几乎无延迟
    - raw: 原始即时输出
    """
    if mode == "normal":
        thinking_effect(thinking_time=2.5, interval=0.5)
        typewriter_print(response, base_delay=0.03, var_delay=0.05, punct_delay=0.4)
    elif mode == "fast":
        typewriter_print(response, base_delay=0.01, var_delay=0.01, punct_delay=0.1)
    elif mode == "raw":
        stream_print(response)
    else:
        raise ValueError("未知模式: 请选择 normal | fast | raw")


user_content = input("Enter your message: ")
# 测试对话
messages = [
    {
        'role': 'user',
        'content': user_content,
    },
]

# 使用 stream=True 开启流式输出
response = chat('deepseek-r1:7b', messages=messages, stream=True)

# 根据需要切换模式
print_response(response, mode="normal")  # normal | fast | raw
