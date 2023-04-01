from chatgpt import ChatGPT
import os

gpt = ChatGPT(os.getenv("OPENAI_KEY"))
while True:
    gpt.chat()
