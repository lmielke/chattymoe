"""
##################### chattymoe MOE #####################
can do whatever you imagine


"""

import yaml, os, re, subprocess
from datetime import datetime as dt
import chattymoe.settings as sts

import colorama as color

color.init()

import openai
openai.api_key = sts.apiKey

from chattymoe.content import Content

class Prompt:
    """[summary]

    [description]
    """

    def __init__(self, *args, verbose: int = 0, **kwargs ) -> None:
        self.verbose = verbose
        self.entry = self.handle_prompt(*args, **kwargs)

    def handle_contents(self, entry, *args, **kwargs):
        ct = Content(*args, **kwargs)
        entry['content'] = ct.get_text(*args, content=entry['content'], **kwargs)
        return entry

    def create_prompt(self, entry=None, *args, role, **kwargs):
        prompt = {'content': '', 'role': role} if entry is None else entry
        return prompt

    def handle_prompt(self, prompt=None, *args, **kwargs):
        if prompt is None:
            prompt = self.create_prompt(*args, **kwargs)
        # prompt.update(self.handle_roles(prompt, *args, **kwargs))
        prompt.update(self.handle_contents(prompt, *args, **kwargs))
        return prompt
