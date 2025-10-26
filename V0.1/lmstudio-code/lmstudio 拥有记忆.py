import re
import lmstudio as lms

model = lms.llm("openai/gpt-oss-20b")
chat = lms.Chat("您是一个专注于任务的 AI 助手")

FINAL_BLOCK_RE = re.compile(
    r"<\|start\|>assistant<\|channel\|>final<\|message\|>(.*?)<\|end\|>",
    re.DOTALL,
)

def clean_prefixes(text: str) -> str:
    # 去掉诸如 "final" / "assistantfinal" / "assistant final" / "assistant:" 等前缀标记
    return re.sub(
        r"^(?:\s*(?:assistant\s*final|assistantfinal|assistant|final)\s*[:：-]?\s*)+",
        "",
        text.strip(),
        flags=re.IGNORECASE,
    )

def extract_final_text(full_text: str) -> str:
    t = full_text

    # 情况A：新格式（出现 assistantfinal 关键词）
    if "assistantfinal" in t:
        after = t.split("assistantfinal", 1)[1]
        return clean_prefixes(after)

    # 情况B：老格式（带 <|channel|>final 标记）
    m = FINAL_BLOCK_RE.search(t)
    if m:
        return clean_prefixes(m.group(1))

    # 情况C：有些模型只吐出 "final" 作为分隔符
    if "\nfinal" in t or t.startswith("final"):
        # 取最后一个 "final" 之后的内容，避免把前面的推理带出来
        parts = t.rsplit("final", 1)
        if len(parts) == 2:
            return clean_prefixes(parts[1])

    # 情况D：兜底清洗（去控制标签与分析段）
    t = re.sub(r"<\|[^>]*\|>", "", t)  # 去掉 <|...|> 控制标签
    # 去掉开头的 analysis...assistant/final 片段
    t = re.sub(r"^analysis.*?(assistant\s*final|assistantfinal|assistant|final)", "", t, flags=re.DOTALL|re.IGNORECASE)
    return clean_prefixes(t)

while True:
    user_input = input("You (leave blank to exit): ")
    if not user_input:
        break

    chat.add_user_message(user_input)
    prediction_stream = model.respond_stream(chat, on_message=chat.append)

    chunks = []
    for fragment in prediction_stream:
        chunks.append(getattr(fragment, "content", str(fragment)))
    full_text = "".join(chunks)
    # print(f"原本的回答：{full_text}")

    answer = extract_final_text(full_text)
    print("Bot: ", end="")
    print(answer)
