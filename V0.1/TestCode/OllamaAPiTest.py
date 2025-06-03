# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 14:46
# @Author  : AI悦创
# @FileName: OllamaAPiTest.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
import requests

API = "http://localhost:11434/api/generate"
payload = {
    "model": "deepseek-r1:7b",
    "prompt": "给我一个贪吃蛇的网页版游戏",
    "stream": False
}
res = requests.post(API, json=payload)
print(res.json())

