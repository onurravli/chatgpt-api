from chatgpt import ChatGPT
import os

gpt = ChatGPT(key = os.getenv("OPENAI_KEY") if os.getenv("OPENAI_KEY") != None else input("Your key: "))
while True:
    gpt.chat()
