# info.py
import chattymoe.settings as sts
from chattymoe.chattymoe import Moe
from chattymoe.content import Content
from chattymoe.response import Response
import pyperclip as pc
import subprocess, time
import colorama as color

color.init()

def communicate(text, *args, lang, **kwargs):
    subprocess.call(['boak', 'say', text, '-l', lang], shell=True)

def text_to_shelly(text, *args, **kwargs):
    import chattymoe.apps.shelly.shelly as shelly
    shelly.main(text, *args, entryPoint='set_shell_in', **kwargs)

def run_chat(*args, **kwargs):
    chattyMoe = Moe(*args, **kwargs)
    chattyMoe.initialize(*args, **kwargs)
    moe = chattyMoe
    # chat = moe.run(*args, **kwargs)
    for mo in moe.run(*args, **kwargs):
        # mo = next(chat)
        process(mo.chat[-1].entry, *args, **kwargs)
        # print(f"\n\n\tchat.run_chat pausing: 2")
        time.sleep(2)

def process(prompt, *args, origin, app, **kwargs):
    if prompt.get('role') == 'user' and origin != 'audio':
        print(f"{color.Fore.YELLOW}user:{color.Style.RESET_ALL} {mo.chat[-1]['content']}")
    elif prompt.get('role') == 'assistant' and app == 'shelly':
        text_to_shelly(prompt['content'].strip(), *args, **kwargs)
    elif prompt.get('role') == 'assistant' and origin == 'audio':
        communicate(prompt['content'], *args, **kwargs)

def main(*args, **kwargs):
    run_chat(*args, **kwargs)

if __name__ == "__main__":
    main()
