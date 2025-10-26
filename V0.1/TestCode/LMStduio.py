# -*- coding: utf-8 -*-
# @Time    : 2025/9/21 14:51
# @Author  : AI悦创
# @FileName: LMStduio.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
# code is far away from bugs with the god animal protecting
#    I love animals. They taste delicious.
import lmstudio as lms

# user_content = input("Enter your message: ")
messages = []

if __name__ == '__main__':
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        messages.append({
            'role': 'user',
            'content': user_input,
        })
        model = lms.llm("deepseek/deepseek-r1-0528-qwen3-8b")
        response = model.respond(user_input)
        print(type(response))

        # 调用逐字打印函数
        # msg_data = stream_print(response, show_think=False)
        # messages.append(msg_data)
