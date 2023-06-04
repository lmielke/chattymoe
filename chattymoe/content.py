# content.py
import chattymoe.settings as sts
import os, subprocess, sys, yaml

import colorama as color

color.init()


class Content:

    def __init__(self, *args, origin, app, **kwargs):
        self.origin = origin
        self.app = app
        self.text = ''

    def get_text(self, *args, content=None, **kwargs):
        if content.strip():
            content = content.strip()
        elif self.origin == 'audio':
            for i in range(3):
                content = self.text_from_audio(*args, **kwargs)
                if content:
                    break
        elif self.app == 'shelly':
            content = self.text_from_shelly(*args, **kwargs)
        elif self.origin == 'input':
            content = input(f"{color.Fore.YELLOW}Enter text: {color.Style.RESET_ALL}: ")
        content = self.clean_content(content, *args, **kwargs)
        return content

    def text_from_audio(self, *args, lang, **kwargs):
        subprocess.call(['boak', 'listen', 'text', '-l', lang], shell=True)
        with open(sts.listen_log, 'r') as f:
            return f.read()

    def clean_content(self, content, *args, **kwargs):
        content = content.replace('<colon>', ': ')#.replace('<newline>', '\n')
        return content

    def text_from_shelly(*args, **kwargs):
        import chattymoe.apps.shelly.shelly as shelly
        out = shelly.main(*args, entryPoint='get_shell_response', **kwargs)
        out = f"PS {out}\n\nType a single powershell command of less than 100 characters!"
        return out