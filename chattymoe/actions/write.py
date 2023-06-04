# info.py
import chattymoe.settings as sts
from chattymoe.chattymoe import Moe
from chattymoe.content import Content
from chattymoe.response import Response
import pyperclip as pc

import colorama as color

color.init()


def write(chattyMoe, *args, chat, model, yes, **kwargs):
    for i, message in enumerate(chat, 1):
        print(f"\n{color.Fore.YELLOW}Message {i} of {len(chat)}:{color.Style.RESET_ALL}")
        for k, vs in message.items():
            if k in sts.msgFields:
                print(f"{color.Fore.GREEN}{k}{color.Fore.RESET}: {vs}")
            else:
                print(f"{color.Fore.CYAN}{k}{color.Fore.RESET}: {vs}")

def main(*args, **kwargs):
    chattyMoe = Moe(*args, **kwargs)
    pr = Content(*args, **kwargs)
    chat = chattyMoe.load_chats(*args, **kwargs)
    chat = chattyMoe.maintain_chat(chat, *args, **kwargs)
    write(chattyMoe, *args, chat=chat, **kwargs)


if __name__ == "__main__":
    main()
