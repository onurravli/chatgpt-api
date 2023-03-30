from chatgpt import ChatGPT
from dotenv import load_dotenv  # It doesn't necessary if you don't use env variables.
import os

load_dotenv()
gpt = ChatGPT(str(os.getenv("KEY")))
while True:
    gpt.chat()
