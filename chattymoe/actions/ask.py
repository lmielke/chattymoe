# info.py
import chattymoe.settings as sts
from chattymoe.chattymoe import Moe
from chattymoe.content import Content
from chattymoe.response import Response
import pyperclip as pc

import colorama as color

color.init()


def ask(chattyMoe, *args, model, yes, **kwargs):
    cleaned = None
    if sending_confirmed(model, yes, *args, **kwargs):
        r = Response(
                        chattyMoe.post(*args, model=model, **kwargs)
                        )
        # print(f"{r.text = }")
        cleaned = r.clean_response(*args, **kwargs)
        # print(f"{cleaned = }")
        pc.copy(cleaned)
    return cleaned

def sending_confirmed(model, yes, *args, chat, **kwargs):
    """
    if -y (yes) flag is set to False, then the user is asked to confirm the content
    before it is sent to openai
    """
    if not yes:
        for msg in chat:
            print(
                f"\nmodel: "
                f"{color.Fore.YELLOW}{model}{color.Style.RESET_ALL}, "
                f"tool: {color.Fore.YELLOW}{msg['meta'][0]}{color.Style.RESET_ALL}, "
                f"verbosity: {color.Fore.YELLOW}{sts.verbosity.get(msg['meta'][1])}"
                f"{color.Fore.WHITE}, -y: {color.Style.RESET_ALL}"
                f"{color.Fore.YELLOW}{yes}"
                f"{color.Fore.WHITE}\nContent: {color.Style.RESET_ALL} "
                f"{color.Fore.YELLOW}{msg['content']}{color.Style.RESET_ALL}"
                )
        return input(f"Send? (y/n): ").lower() == 'y'
    return yes

def get_chat(chattyMoe, *args, **kwargs):
    pr = Content(*args, **kwargs)
    chat = chattyMoe.load_chat(*args, **kwargs)
    chat = chattyMoe.maintain_chat(chat, *args, **kwargs)
    return chat

def main(*args, **kwargs):
    print(kwargs)
    chattyMoe = Moe(*args, **kwargs)
    # chat = get_chat(chattyMoe, *args, **kwargs)
    answer = ask(chattyMoe, *args, **kwargs)



if __name__ == "__main__":
    main()
