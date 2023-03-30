import sys
from time import sleep
import requests
import json


class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class ChatGPT:
    def __init__(self, key: str):
        self.key = key

    def send(self, model: str, msg: str, role: str, temp: float):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }
        data = {
            "model": model,
            "messages": [{"role": role, "content": msg}],
            "temperature": temp,
        }

        try:
            resp = requests.post(url, headers=headers, data=json.dumps(data))
            return json.loads(resp.text)["choices"][0]["message"]["content"]
        except KeyError:
            return json.loads('{"Error": "An key error occurred."}')
        except:
            return json.loads('{"Error": "An unknown error occurred."}')

    def typewriter(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        print("")

    def chat(self, *args):
        try:
            question = input(colors.HEADER + "Q: " + colors.ENDC)
            if question == "!exit":
                sys.exit(0)
            print(colors.OKBLUE + "A: " + colors.ENDC, end="")
            resp = ""
            if len(args) > 1:
                model: str = args[0] if args[0] != (None or "") else "gpt-3.5-turbo"
                role: str = (
                    args[1]
                    if (len(args) > 2 and args[1] != (None or ""))
                    else "assistant"
                )
                temp: float = (
                    args[2] if (len(args) > 3 and args[2] != (None or "")) else 0.5
                )
                try:
                    resp = self.send(model, question, role, temp)
                except Exception as e:
                    print(colors.FAIL + f"An error occurred: {e}" + colors.ENDC)
                    sys.exit(-1)
            else:
                try:
                    resp = self.send("gpt-3.5-turbo", question, "assistant", 0.7)
                except:
                    print(colors.FAIL + "An error occurred." + colors.ENDC)
            self.typewriter(resp)
        except (KeyboardInterrupt, EOFError):
            print(colors.WARNING + f"\nExiting" + colors.ENDC)
            sys.exit(0)
