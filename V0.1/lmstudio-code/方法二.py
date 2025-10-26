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
    message_count = 0  # 计数器
    text = ""
    for fragment in prediction_stream:
        text += str(fragment.content)
        if "<|message|>" in fragment.content:
            message_count += 1
            # 当计数大于1时，正常输出，不显示分析标记
        elif message_count == 2:
            print(fragment.content, end="", flush=True)
    print()
    print(f"原本：{text}")
