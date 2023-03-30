from chatgpt import ChatGPT
from dotenv import load_dotenv # Just for env. variables.
import os

load_dotenv()
gpt = ChatGPT(str(os.getenv("KEY")))
while True:
    gpt.chat()
