from ollama import chat
import time


def thinking_effect(thinking_time=2.0, interval=0.5):
    """思考中... 效果"""
    print("思考中", end='', flush=True)
    start = time.time()
    while time.time() - start < thinking_time:
        print(".", end='', flush=True)
        time.sleep(interval)
    print("\n")


think_count = 0


def stream_print(response):
    global think_count
    global think_switch
    result = ''
    for messages in response:
        if think_switch == 0:
            if think_count == 2:
                print(messages['message']['content'], end='', flush=True)
                result += messages['message']['content']
            if messages['message']['content'] == '<think>' or messages['message']['content'] == '</think>':
                think_count += 1
        else:
            print(messages['message']['content'], end='', flush=True)
            result += messages['message']['content']
    result += '\n'
    return result


think_switch = int(input('是否开启思维链显示(是输入1，否输入0)：'))

messages = []

while True:
    user_input = input('\n用户输入：')
    response = chat('deepseek-r1:7b', messages=[*messages, {'role': 'user', 'content': user_input}], stream=True)

    # thinking_effect()
    rep = stream_print(response=response)
    messages += [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': rep},
    ]
