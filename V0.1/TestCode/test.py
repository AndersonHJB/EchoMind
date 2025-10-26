# -*- coding: utf-8 -*-
# @Time    : 2025/10/19 14:12
# @Author  : AI悦创
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
import lmstudio as lms

# model = lms.llm()
model = lms.llm("openai/gpt-oss-20b")
chat = lms.Chat("您是一个专注于任务的 AI 助手")

while True:
    user_input = input("You (leave blank to exit): ")

    if not user_input:
        break
    chat.add_user_message(user_input)
    prediction_stream = model.respond_stream(
        chat,
        on_message=chat.append,
    )
    print("Bot: ", end="", flush=True)
    for fragment in prediction_stream:
        print(fragment.content, end="", flush=True)
    print()
