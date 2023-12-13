# Readme

<img src="https://drive.google.com/uc?id=1C8LBRduuHTgN8tWDqna_eH5lvqhTUQR4" alt="me_happy" class="plain" height="150px" width="220px">

## ChattyMoe
NOTE: This is a terrible prototype and not ready for use. It is currently in development
    and currently only working with Windows powershell.

Also some features such as content.text_from_audio are run as subprocess and are not
available in this package. Reuse any code as you like.



ChattyMoe is a python application that authonomously builds python applications. It uses the OpenAI API to generate project structurs and codes python modules. It is currently in development and not ready for use.

ChattyMoe is called via chattymoe.actions with the provided arguments. The action then calls the 'chattymoe.chattymoe' module which uses the OpenAI API to generate content. The content is then used to generate a python project structure. The project structure is then used to generate python code.

## get and install
```
git clone git@gitlab.com:larsmielke2/chattymoe.git
```

### run in Shell
chattymoe is run using an action from chattymoe.actions.actionName

Examples:
```
    moe info
    moe $action -a $application -v $verbose -y -r # -r for un-modified raw content
    moe 'how to list files from current directory' -a powershell -v 2 -y

    # be extra careful when running
    moe auto -a shelly -c auto_python [-y]
```

## install
- check and or update Pipfile/requirements.txt
- pipenv install [-d] NOTE: some dev packages are not available to you, so run without -d
- pipenv shell
- add your openAi apiKey to chattymoe.settings.py or diretly to chattymoe.api_key.py -> get_api_key
- at this point "moe info" should return some package meta data and the project structure
- run commands from above


## Project Structure
The chattymoe package uses a '__main__.py' entrypoint which calls an action from the 'chattymoe.actions' package.

projectDir: ~/python_venvs/libs/chattymoe
chattymoe
├───chattymoe
│   ├───actions
│   │
│   ├───logs
│   └───test
│       ├───data
│       ├───logs
│
└───media
    └───chats

- coding is in chattymoe/chattymoe folder, add your .py files there
- __main__.py calls chattymoe/chattymoe/actions/someaction.py [provides as shell call args]

## USAGE
1. activate your environemnt
2. test openAi availability: pipenv run ping
3. moe 'how are you today' -r
4. NOTE: the answer is in your clipboad now




# ChatGPT






<chatgpt>
## Moe project info 
[metadata]
name = chattymoe
include_package_data = True
version = 0.0.1
description = chatGpt based coding engine
long_description = file: README.md, CHANGELOG.md, LICENSE
long_description_content_type = text/markdown
author = Lars Mielke
author_email = info@while-ai.org
url = https://gitlab.com/larsmielke2/chattymoe

[options]
py_modules = chattymoe
install_requires = 
    colorama
    pyyaml
    requests
    tabulate
packages = find:

[options.entry_points]
console_scripts =
    moe = chattymoe.__main__:main

                    |--chattymoe/
                        |--.env
                        |--.gitignore
                        |--.gitlab-ci.yml
                        |--.pre-commit-config.yaml
                        |--CHANGELOG.md
                        |--dall_e_img_gen.py
                        |--graph
                        |--graph.svg
                        |--LICENSE
                        |--MANIFEST.in
                        |--myFile.txt
                        |--Pipfile
                        |--Pipfile.lock
                        |--pyproject.toml
                        |--Readme.md
                        |--setup.cfg
                        |--setup.py
                        |--tox.ini
                        |--ws_moe.sublime-project
                        |--ws_moe.sublime-workspace
                        |--__init__.py
                        |--chattymoe/
                            |--api_key.py
                            |--arguments.py
                            |--chattymoe.py
                            |--content.py
                            |--contracts.py
                            |--get_creds.py
                            |--project_state.py
                            |--prompt.py
                            |--response.py
                            |--settings.py
                            |--__init__.py
                            |--__main__.py
                            |--actions/
                                |--ask.py
                                |--auto.py
                                |--chat.py
                                |--info.py
                                |--state.py
                                |--write.py
                                |--__init__.py
                            |--apps/
                                |--process.yml
                                |--shelly/
                                    |--shelly.py
                            |--helpers/
                                |--general.py
                                |--markddown_to_python.py
                            |--test/
                                |--test_chat.py
                                |--test_chattymoe.py
                                |--test_content.py
                                |--test_markdown_to_pyhton.py
                                |--test_prompt.py
                                |--test_response.py
                                |--__init__.py
                                |--data/
                                    |--chattymoe.yml
                                    |--response.txt
                                    |--test_content.yml
                                    |--test_markdown_to_python_testfile.md
                                    |--test_markdown_to_python_testfile.py
                                |--testopia_logs/
                                    |--2023-12-04-20-45-18-263428_test_chat.log
                                    |--2023-12-04-20-45-56-391273_test_chattymoe.log
                        |--media/
                            |--chats/
                                |--auto_python.yml
                                |--empty.yml
                                |--pythoncode.yml
                                |--python_developer.yml
                                |--test_chat.yml
                            |--templates/
                                |--Readme.md
############### dall_e_img_gen.py ################
```python
# openai_list.py 04_17_2023__11_52_47
	import os, sys, time
	print(sys.executable)
	
	#RUN like: 
	# python  C:\Users\lars\python_venvs\libs\chattymoe\openai_list.py
	import chattymoe.settings as sts
	import openai
	openai.api_key = sts.apiKey
	
	prompts = {
	    'cat': """A terribly scared cat jumping up to escape from a tiny mouse.
	                photo realistic, professional camera
	                """,
	    'roster': """
	            A angry rooster side view head to shoulder. kali linux style, fine lines, 
	            neon green red and blue before a black background. minimalistic, professional, 
	            fine lines, almost invisible, watermark neon lighting green blue red, fine 
	            line drawing, black background
	            """,
	}
	# 40.2023 bad results compared to mj
	print(openai.Image.create(
	    prompt=prompts['cat'].replace('\n', ' '),
	    n=1,
	    size="1024x1024",
	    ))
	
```

#################### Pipfile #####################
```
[[source]]
	url = "https://pypi.org/simple"
	verify_ssl = true
	name = "pypi"
	
	[packages]
	colorama = "*"
	pyyaml = "*"
	requests = "*"
	tabulate = "*"
	chattymoe = {editable = true, path = "."}
	openai = "*"
	pyperclip = "*"
	jinja2 = "*"
	graphviz = "*"
	
	[dev-packages]
	black = "*"
	pre-commit = "*"
	logunittest = {editable = true, path = "/Users/Lars/python_venvs/packages/logunittest"}
	joringels = {editable = true, path = "C:/Users/Lars/python_venvs/libs/joringels"}
	
	[requires]
	python_version = "3.11"
	
	[scripts]
	ping = "moe 'ping, if you can read me, say pong' -r -y"
	
```

################### setup.cfg ####################
```
[metadata]
	name = chattymoe
	include_package_data = True
	version = 0.0.1
	description = chatGpt based coding engine
	long_description = file: README.md, CHANGELOG.md, LICENSE
	long_description_content_type = text/markdown
	author = Lars Mielke
	author_email = info@while-ai.org
	url = https://gitlab.com/larsmielke2/chattymoe
	
	[options]
	py_modules = chattymoe
	install_requires = 
	    colorama
	    pyyaml
	    requests
	    tabulate
	packages = find:
	
	[options.entry_points]
	console_scripts =
	    moe = chattymoe.__main__:main
	
```

#################### setup.py ####################
```python
from setuptools import setup
	
	setup(include_package_data=True)
	
```

################## __init__.py ###################
```python

```

################### api_key.py ###################
```python
"""
	This returns the openai api key
	NOTE: This uses a password tool which is not available to you! So you have to replace
	the content of this get_api_key with your openai api key retrieval.
	"""
	
	from joringels.src.actions import fetch
	
	def get_api_key():
	    """
	    provides your API key using joringels api
	    NOTE: 
	    if you dont use joringels or any other password tool,
	    you can remove the content of this function and return your api-key directly instead:
	    return "apiKey as proviced by openai"
	    """
	    creds = {
	            'safeName': 'digiserver',
	            'entryName': 'chatgptApi',
	    }
	
	    # add your openAi API-key here as a string
	    return fetch.alloc(**creds, retain=True).get('password').strip()
```

################## arguments.py ##################
```python
"""
	    pararses chattymoe arguments and keyword arguments
	    args are provided by a function call to mk_args()
	    
	    RUN like:
	    import chattymoe.arguments
	    kwargs.updeate(arguments.mk_args().__dict__)
	"""
	import argparse
	
	
	def mk_args():
	    parser = argparse.ArgumentParser(description="run: python -m chattymoe info")
	    parser.add_argument(
	        "action", metavar="action", nargs=None, help="chattymoe.actions/chats or a prompt"
	    )
	    parser.add_argument(
	        "-l",
	        "--lang",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default='en',
	        help="language to use",
	    )
	
	    parser.add_argument(
	        "-m",
	        "--model",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default="gpt-3.5-turbo",
	        help="openAi model to use",
	    )
	
	    parser.add_argument(
	        "-c",
	        "--chat",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default='empty',
	        help="chat template you want to use, see settings.chatsDir",
	    )
	
	    parser.add_argument(
	        "-p",
	        "--cwd",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default='C:/temp',
	        help="workPath/working directory to use moe in",
	    )
	
	    parser.add_argument(
	        "-o",
	        "--origin",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default='action',
	        help="default source / origin of prompt i.e. action, audio, text, system",
	    )
	
	    parser.add_argument(
	        "-a",
	        "--app",
	        required=False,
	        nargs=None,
	        const=None,
	        type=str,
	        default=None,
	        help="app to use chat for i.e. see settings.appsDir",
	    )
	
	    parser.add_argument(
	        "-t",
	        "--test",
	        required=False,
	        nargs="?",
	        const=True,
	        type=bool,
	        default=False,
	        help="test response, for testing you can enter chatgpts expected response",
	    )
	
	    parser.add_argument(
	        "-v",
	        "--verbose",
	        required=False,
	        nargs="?",
	        const=1,
	        type=int,
	        default=1,
	        help="rewpond with - 1:no explanation, 2:short explanation, 3:detailed explanation",
	    )
	
	    parser.add_argument(
	        "-y",
	        "--yes",
	        required=False,
	        nargs="?",
	        const=True,
	        type=bool,
	        default=False,
	        help="send prompt without user confirmation",
	    )
	
	    parser.add_argument(
	        "-r",
	        "--raw",
	        required=False,
	        nargs="?",
	        const=True,
	        type=bool,
	        default=False,
	        help="send prompt as typed without any modifications",
	    )
	
	    return parser.parse_args()
	
```

################## chattymoe.py ##################
```python
"""
	##################### chattymoe MOE #####################
	can do whatever you imagine
	
	
	"""
	
	import yaml, os, re, subprocess, time
	from datetime import datetime as dt
	import chattymoe.settings as sts
	import chattymoe.helpers.general as hlp
	from tabulate import tabulate as tb
	import colorama as color
	
	color.init()
	_RED = color.Fore.RED
	_YELLOW = color.Fore.YELLOW
	_GREEN = color.Fore.GREEN
	_CYAN = color.Fore.CYAN
	_BLUE = color.Fore.BLUE
	_WHITE = color.Fore.WHITE
	_NONE = color.Style.RESET_ALL
	
	
	import openai
	openai.api_key = sts.apiKey
	
	from chattymoe.prompt import Prompt
	
	class Moe:
	    """[summary]
	
	    [description]
	    """
	
	    def __init__(self, *args, verbose: int = 0, **kwargs ) -> None:
	        self.verbose = verbose
	        self.running = False
	        self.chat, self.comments = self.load_chat(*args, **kwargs)
	
	    def post(self, *args, model, **kwargs):
	        """
	        Sends message to openai and handles the response.
	        """
	        r = openai.ChatCompletion.create(
	            model=model, 
	            messages=[{f: ct for f, ct in m.entry.items() if f in sts.msgFields} for m in self.chat]
	            )
	        self.chat.append(Prompt(r['choices'][-1]['message'], *args, **kwargs))
	        self.print_message(*args, **kwargs)
	        return r
	
	    def print_message(self, *args, **kwargs):
	        print(f"{_WHITE}assi:")
	        assiMsg = {
	                    'assi_in': hlp.insert_newline(self.chat[-2].entry.get('content')), 
	                    'assi_out': [self.chat[-1].entry.get('content')], 
	                    'lenChat': [len(self.chat)],
	                    }
	        assiMsg = tb(assiMsg, headers='keys', tablefmt='github')
	        for line in assiMsg.split('\n'): print(f"\t{_YELLOW}{line}{_NONE}")
	        time.sleep(5)
	
	
	    def load_chat(self, *args, chat, **kwargs):
	        """
	        loads chats and comments
	        chat: dict - chat history to prime the model with
	        comments: dict - comments to add to the chat history and the chat going forward
	        """
	        fileName = f"{chat}.yml" if f"{chat}.yml" in os.listdir(sts.chatsDir) else sts.empty
	        with open(os.path.join(sts.chatsDir, fileName), 'r') as f:
	            params = yaml.safe_load(f)
	        chat, comments = params['chat'], params.get('comments')
	        if chat is None:
	            self.running = True
	        return chat, comments
	    
	    def confirm(self, *args, yes=False, **kwargs):
	        if self.chat[-1].entry.get('content').strip().lower() in ['stop', 'stopp']:
	            print(f"{_RED}User stopped the program{_NONE}")
	            self.running = False
	            return False
	        if not yes:
	            print(f"{_YELLOW}Moe.confirm: {_NONE}{self.chat[-1].entry = }")
	            test = input("Test: ")
	            userInput = input(f"Send/Stop? (y/stop): ").lower()
	            exit()
	            if userInput == 'y':
	                return True
	            elif userInput == 'stop':
	                raise Exception("User stopped the program")
	        return yes
	
	    def check_exit_condition(self, *args, **kwargs):
	        if cmd.lower() in ['stop', 'stopp']:
	            raise Exception("User stopped the program")
	
	    def initialize(self, *args, **kwargs):
	        for i, prompt in enumerate(self.chat):
	            self.chat[i] = Prompt(prompt, *args, **kwargs)
	        self.running = True
	
	    def check_correctness(self, *args, **kwargs):
	        if len(self.lastAnswer) > sts.psMaxLen:
	            return False, f"Answer too long! max: {sts.psMaxLen}"
	        if '\n' in self.lastAnswer.strip():
	            return False, f"Answer must be a single line!"
	        return True, 'OK'
	
	    def run(self, *args, **kwargs):
	        # clean content for eve3ry chat entry
	        while self.running:
	            # prepare next prompt for futur yield
	            if self.chat[-1].entry.get('role') not in ['user', 'system']:
	                self.chat.append(Prompt(*args, **kwargs))
	            if self.confirm(*args, **kwargs):
	                self.post(*args, **kwargs)
	            yield self
	
	
	    def __str__(self, *args, **kwargs):
	        dotPath = f"{__file__.replace(sts.projectDir, '').replace(os.sep, '.')}"
	        return dotPath.strip('.')
	
```

################### content.py ###################
```python
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
```

################## contracts.py ##################
```python
# contracts.py
	import chattymoe.settings as sts
	import os, sys
	import colorama as color
	
	color.init()
	
	
	def checks(*args, **kwargs):
	    kwargs['action'], kwargs['chat'] = verify_is_action(*args, **kwargs)
	    kwargs['verbose'] = verify_verbosity(*args, **kwargs)
	    kwargs['role'] = handle_roles(*args, **kwargs)
	    return kwargs
	
	
	def verify_is_action(*args, action, chat, verbose, **kwargs):
	    """
	    The action kwarg can either contain a callable action (module) from chattymoe.actions
	    or it can contain a chat (fileName) or role (string).
	    If the action kwarg contains a chat or role, those must be moved to a 'role' kwarg
	    In those cases the actual action kwarg defaults to ask or chat.
	    NOTE:   This construct seems somewhat arbitrary but was necessary to allow simple
	            user input to be passed to the chat i.e. run a action or ask a role.
	    """
	    actions = os.listdir(sts.actionsPath)
	    chats = os.listdir(sts.chatsDir)
	    if f"{action}.py" in actions:
	        return action, chat
	    elif f"{action}.yml" in chats:
	        return 'chat', action
	    else:
	        return 'chat', action
	
	def verify_verbosity(*args, verbose, raw, action, **kwargs):
	    """
	    If raw text is send to openAi, verbosity is not defined, because verbose will
	    be translated into a added phrase (str) as defined by sts.verbosity dictionary
	    Using None sts.verbosity.get will return None and no phrase is added to the role
	    """
	    if raw:
	        return None
	    elif action == 'write':
	        # verbosity is changed to 1 to allow proper role construction, see sts.verbosity 
	        msg = f"contracts.verify_verbosity: changing verbosity to 1. Still not posted"
	        print(f"{color.Fore.YELLOW}{msg}{color.Style.RESET_ALL}")
	        return 1
	    else:
	        return verbose
	
	def handle_roles(*args, app=None, role=None, **kwargs):
	    role = sts.apps[app].get('role')
	    return role
```

################## get_creds.py ##################
```python
# get_creds.py
	import os, sys
	from getpass import getpass as gp
	import colorama as color
	
	color.init()
	
	
	class Creds:
	    def __init__(self, *args, **kwargs):
	        self.rules = None  # implement key rules here
	
	    def set(self, msg="key", *args, force=True, confirmed=True, key=None, **kwargs):
	        key = self.get(key, *args, **kwargs)
	        if not key:
	            key = None
	            while not key:
	                key = gp(content=f"{msg.strip(': ')}: ", stream=None)
	                if force == False:
	                    break
	            while not confirmed:
	                confirmed = self._confirm_equals(key, *args, **kwargs)
	        key = self.get(key, *args, **kwargs)
	        return key
	
	    def get(self, key, *args, safeName=None, **kwargs):
	        if key == "os":
	            msg = f"\tUsing $env:key {safeName}"
	            key = os.environ["DATASAFEKEY"]
	            print(f"{color.Fore.YELLOW}{msg}{color.Style.RESET_ALL}")
	        return key
	
	    def _confirm_equals(self, key, *args, **kwargs):
	        # getting new key
	        confirmKey = None
	        while confirmKey != key:
	            confirmKey = gp(content=f"re-type key to continue: ", stream=None)
	        return True
	
```

################ project_state.py ################
```python
# statefile.py
	import os, shutil
	from jinja2 import Environment, FileSystemLoader
	import chattymoe.settings as sts
	
	
	class Template:
	    """Generates a statefile and places it into the correct product folder
	
	    [description]
	    """
	
	    def __init__(self, *args, verbose: int = 0, **kwargs ) -> None:
	        self.verbose = verbose
	
	    def generate_statefiles(self, buildFiles=None, *args, service=None, **kwargs) -> None:
	        for buildLevel, genParams in buildFiles.items():
	            docf = self.gen_from_template(*args, **genParams.get('template'), **kwargs)
	            # safe gen result and copy it to Dockerilfe repo
	            with open(genParams.get('tgt'), 'w') as t:
	                t.write(docf)
	            # only the _up files need to be copied to state_ups to be used by compose
	            if buildLevel == sts.phases.get(service, [None])[-1]:
	                self.copy_statefile(genParams, *args, **kwargs)
	
	    def gen_from_template(self, *args, templatePath:str, params:dict, **kwargs) -> None:
	        #target, template, tParams, dataSource, data
	        env = Environment(loader=FileSystemLoader([os.path.dirname(templatePath)]))
	        return env.get_template(os.path.basename(templatePath)).render(params=params)
	
	    def copy_statefile(self, genParams, *args, **kwargs) -> None:
	        shutil.copyfile(
	                        genParams.get('tgt'),
	                        os.path.join(sts.stateUpsDir, genParams.get('buildId')),
	                        )
	
	    def __str__(self, *args, **kwargs):
	        dotPath = f"{__file__.replace(sts.projectPath, '').strip(os.sep).replace(os.sep, '.')}"
	        return dotPath
	
```

################### prompt.py ####################
```python
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
	
```

################## response.py ###################
```python
# response.py
	import chattymoe.settings as sts
	import re
	import colorama as color
	
	color.init()
	
	class Response:
	
	    def __init__(self, response=None, *args, **kwargs):
	        self.response = response
	        self.text = self._to_text(*args, **kwargs)
	
	    def _to_text(self, *args, **kwargs):
	        if self.response is None:
	            msg = f"{color.Fore.RED}No response to convert to text!{color.Style.RESET_ALL}"
	            raise Exception(msg)
	        elif isinstance(self.response, str):
	            return self.response
	        else:
	            return self.response.choices[0].to_dict()['message']['content']
	
	    def clean_response(self, *args, **kwargs):
	        """
	        openAi s response might contain code which wrapped in code blocks <code> </code>,
	        this gets the content of those code blocks and returns them as string
	        """
	        # cleaned = self.text.replace('\"', "'").replace("```", "").strip()
	        # sometimes openAi uses \ instead of / to end a code block
	        cleaned = self.text.replace(sts.misSpell, sts.codeEnd)
	        if sts.codeStart in cleaned:
	            cleaned = cleaned.split(sts.codeStart)[1].split(sts.codeEnd)[0]
	        return cleaned.strip()
```

################## settings.py ###################
```python
# settings.py
	import os, sys, time, yaml
	from chattymoe.api_key import get_api_key
	
	packageName = 'chattymoe'
	packageDir = os.path.dirname(__file__)
	projectDir = os.path.dirname(packageDir)
	
	actionsPath = os.path.join(packageDir, "actions")
	testPath = os.path.join(packageDir, "test")
	logsPath = os.path.join(packageDir, "logs")
	ressourcesPath = os.path.join(packageDir, "ressources")
	
	testPath = os.path.join(packageDir, "test")
	testDataDir = os.path.join(testPath, "data")
	
	mediaDir = os.path.join(projectDir, "media")
	chatsDir = os.path.join(mediaDir, "chats")
	templatesDir = os.path.join(mediaDir, "templates")
	
	helpersDir = os.path.join(packageDir, 'helpers')
	appsDir = os.path.join(packageDir, 'apps')
	prcLogPath = os.path.join(appsDir, 'process.yml')
	
	listen_log = "C:/Users/lars/python_venvs/modules/speaker/listen_log.txt"
	
	def unalias_path(workPath: str) -> str:
	    """
	    repplaces path aliasse such as . ~ with path text
	    """
	    workPath = workPath.replace(r"%USERPROFILE%", "~")
	    workPath = workPath.replace("~", os.path.expanduser("~"))
	    if workPath.startswith(".."):
	        workPath = os.path.join(os.path.dirname(os.getcwd()), workPath[3:])
	    elif workPath.startswith("."):
	        workPath = os.path.join(os.getcwd(), workPath[2:])
	    return os.path.abspath(workPath).replace(os.sep, "/")
	
	# as by chatGpt 
	def remove_aliases(path):
	    """
	    Removes all aliasse such as ~ . .. from a os.path string
	    """
	    return os.path.abspath(os.path.realpath(path)).replace(os.sep, "/")
	
	# you can add the api_key here as string, NOTE: if you do this, remove the get_api_key import
	apiKey = get_api_key()
	
	msgFields = ['content', 'role', 'created']
	
	# points of interest
	poi = {
	            'powershell': {'role': 'programmer', 'responseObj': 'code'},
	            'chrome': {'role': 'user', 'responseObj': 'steps'},
	            'python': {'role': 'programmer', 'responseObj': 'code'},
	            }
	
	verbosity = {
	    1: 'no comments and no explanations',
	    2: 'a very short explanation',
	    3: 'a detailed explanation',
	}
	
	codeStart = '<code>'
	codeEnd = '</code>'
	misSpell = r'<\code>'
	
	empty = 'empty.yml'
	
	
	greetings = 'Hello there!'
	
	
	quest = lambda content, poi, application, verbose: (
	                    f"I am working with {application}! How can I '{content}' ? "
	                    f"Give me only the {poi[application].get('responseObj')} "
	                    f"with {sts.verbosity.get(verbose)}! "
	                    f"Highight code blocks with <code> code goes here </code> tags, "
	                    f"so I can easyly copy it."
	                    )
	
	psHistFileName = 'psHist.log'
	psTestPath = 'C:/temp'
	psMaxLen = 100
	encodings = [
	                'utf-8', 'utf-16', 'utf-32', 'utf-16-be', 'utf-16-le', 'utf-32-be',
	                'utf-32-le', 'latin-1', 'ascii', 'cp1252', 'cp437', 'cp850', 'cp852',
	                'cp855', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp865', 'cp866',
	                'cp869', 'cp874', 'cp932', 'cp949', 'cp950', 'cp1006', 'cp1026', 'cp1140',
	                'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257',
	                'cp1258', 'cp65001', 'big5', 'big5hkscs', 'cp037', 'cp424', 'cp437', 'cp500',
	                'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857',
	                'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 'cp866',
	                'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006', 'cp1026',
	                'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255',
	                'cp1256', 'cp1257', 'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
	                'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz',
	                'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
	                'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2',
	                'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8',
	                'iso8859_9', 'iso8859_10', 'iso8859_13', 'iso8859_14',
	                ]
	
	apps = {
	    None: {'role': 'user'},
	    'shelly': {'source': ['powershell', '-Command',], 'role': 'system'},
	}
```

################## __init__.py ###################
```python
# __init__.py
	
```

################## __main__.py ###################
```python
"""
	    Entry poiont for chattymoe shell calls 
	    ###################################################################################
	    
	    __main__.py imports the action module from chattymoe.actions >> actionModule.py
	                and runs it
	                action is provided as first positional argument
	
	    ###################################################################################
	    
	    example: 
	        python -m chattymoe info
	    above cmd is identical to
	        python -m chattymoe.actions.info
	
	
	"""
	
	import colorama as color
	
	color.init()
	import importlib
	
	import chattymoe.settings as sts
	import chattymoe.arguments as arguments
	import chattymoe.contracts as contracts
	
	
	def runable(*args, action, **kwargs):
	    """
	    imports action as a package and executes it
	    returns the runable result
	    """
	    return importlib.import_module(f"chattymoe.actions.{action}")
	
	
	def main(*args, **kwargs):
	    """
	    to runable from shell these arguments are passed in
	    runs action if legidemit and prints outputs
	    """
	    kwargs = arguments.mk_args().__dict__
	
	    # kwargs are vakidated against enforced contract
	    kwargs = contracts.checks(*args, **kwargs)
	    if kwargs.get("action") != "help":
	        return runable(*args, **kwargs).main(*args, **kwargs)
	
	
	if __name__ == "__main__":
	    main()
	
```

##################### ask.py #####################
```python
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
	
```

#################### auto.py #####################
```python
# info.py
	# import chattymoe.settings as sts
	import chattymoe.actions.chat as chat
	import chattymoe.apps.shelly.shelly as shelly
	import time
	
	import colorama as color
	
	color.init()
	
	from time import sleep
	from multiprocessing.pool import Pool
	from multiprocessing import Process, Manager
	
	def main(*args, **kwargs):
	    # manager = Manager()
	    p1 = Process(target=shelly.main, args=args, kwargs=kwargs)
	    p2 = Process(target=chat.main, args=args, kwargs=kwargs)
	    print(f"{color.Fore.CYAN}Starting p1{color.Style.RESET_ALL}")
	    p1.start()
	    print(f"{color.Fore.CYAN}Waiting for p1 to start{color.Style.RESET_ALL}")
	    time.sleep(3)
	    print(f"{color.Fore.CYAN}Starting p2{color.Style.RESET_ALL}")
	    p2.start()
	    p1.join()
	    p2.join()
	    print("Join done")
	
	if __name__ == '__main__':
	    main()
```

#################### chat.py #####################
```python
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
	
```

#################### info.py #####################
```python
# info.py
	import chattymoe.settings as sts
	from chattymoe.chattymoe import Moe
	import subprocess
	import os, re, sys
	
	import colorama as color
	
	color.init()
	
	ignoreDirs = {'.git', 'build', 'dist', 'logs', 'chattymoe.egg-info', '__pycache__'}
	
	def generate_folder_tree(projectDir, ignoreDirs, *args, **kwargs):
	    project_structure = ''
	    indent = '    '
	    for root, dirs, files in os.walk(projectDir):
	        dirs[:] = [d for d in dirs if d not in ignoreDirs]
	        project_structure += f"{indent * (root.count(os.sep))}|--{os.path.basename(root)}/\n"
	        sub_indent = indent * (root.count(os.sep) + 1)
	        for file in files:
	            project_structure += f"{sub_indent}{'|'}--{file}\n"
	    return project_structure
	
	def get_package_info(*args, **kwargs):
	    msg = f"""{f"## Moe project info "}"""
	    print(f"{color.Fore.GREEN}{msg:#^80}{color.Style.RESET_ALL}")
	    with open(os.path.join(sts.projectDir, "setup.cfg"), "r") as f:
	        info = f.read()
	    return f"{msg}\n{info}"
	
	def read_files(*args, **kwargs):
	    """
	        reads python files and includedNonPythonFiles while ignoring 
	        files from ignoreDirs set. Yields file contents.
	    """
	    includedNonPythonFiles = ['Pipfile', 'setup.cfg', 'Manifest.in', ]
	    for root, dirs, files in os.walk(sts.projectDir):
	        dirs[:] = [d for d in dirs if d not in ignoreDirs]
	        for file in files:
	            if file in includedNonPythonFiles or file.endswith('.py'):
	                with open(os.path.join(root, file), 'r') as f:
	                    content = f.read()
	                    content = content.replace('\n', '\n\t')
	                    # replace characters that could break the markdown syntax
	                    if file.endswith('.py'):
	                        content = f"```python\n{content}\n```"
	                    else:
	                        content = f"```\n{content}\n```"
	                    yield f"{f' {file} ':#^50}", content
	
	def mk_readme_md_appendix(*args, **kwargs):
	    """
	    cheates an appendix to the Readme.md file consisting of 
	    the get_package_info, generate_folder_tree
	    then adds the fileNames and fileContent like so:
	    ######### fileName ########
	    fileContent
	    
	    ######### fileName ########
	    ...
	    """
	    startTag, readme = "<chatgpt>", "Readme.md"
	    fileTexts = []
	    for fileName, fileContent in read_files(*args, **kwargs):
	        fileTexts.append(f"{fileName}\n{fileContent}")
	    fileText = '\n\n'.join(fileTexts)
	
	    appendix = (
	                f"\n\n{startTag}\n"
	                f"{get_package_info(*args, **kwargs)}\n"
	                f"{generate_folder_tree(sts.projectDir, ignoreDirs, *args, **kwargs)}"
	                f"{fileText}\n"
	                f"\n</chatgpt>\n"
	                )
	    # opens Readme.md finds start startTag tag and replaces all until the end </chatgpt> tag
	    # C:\Users\lars\python_venvs\libs\chattymoe\Readme.md
	    filePath = os.path.join(sts.projectDir, readme)
	    with open(filePath, "r") as f:
	        readme = f.read()
	    # get index of startTag tag and truncate readme content at beginning of string
	    readme = readme[:readme.find(startTag)] + appendix
	    with open(filePath, "w") as f:
	        f.write(readme)
	
	def main(*args, **kwargs):
	    project_structure = get_package_info(*args, **kwargs)
	    projectDir = sts.projectDir
	    project_structure += '\n## Project Structure\n'
	    project_structure += f"projectDir: {projectDir}\n"
	    project_structure += f"packageDir: {sts.packageDir}\n"
	    project_structure += f"{generate_folder_tree(projectDir, ignoreDirs, *args, **kwargs)}\n"
	    project_structure += f"ignoreDirs: {ignoreDirs}\n"
	    mk_readme_md_appendix(*args, **kwargs)
	    return project_structure
	
	if __name__ == '__main__':
	    out = main()
	    print(project_structure)
	
```

#################### state.py ####################
```python
# info.py
	import chattymoe.settings as sts
	from chattymoe.chattymoe import Moe
	import subprocess
	import os, sys
	
	import colorama as color
	
	color.init()
	
	
	def main(*args, workingDir=None, **kwargs):
	    workingDir = workingDir if workingDir is not None else os.getcwd()
	    print(f"\npackageDir: {sts.packageDir}")
	    print('\ntree:')
	    subprocess.call(f"tree /F {workingDir}".split(), shell=True)
	
	
	if __name__ == "__main__":
	    main()
	
```

#################### write.py ####################
```python
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
	
```

################## __init__.py ###################
```python
# __init__.py
	
```

################### shelly.py ####################
```python
# shelly.py
	"""
	python ./chattymoe/apps/shelly/shelly.py
	NOTE: to stop type quit in chattymoe.apps.shelly.in.log
	"""
	
	import subprocess
	import os, re, shlex, sys, time, yaml
	from datetime import datetime as dt
	import chattymoe.settings as sts
	import chattymoe.helpers.general as hlp
	
	from tabulate import tabulate as tb
	import colorama as color
	
	color.init()
	_RED = color.Fore.RED
	_CYAN = color.Fore.CYAN
	_YELLOW = color.Fore.YELLOW
	_GREEN = color.Fore.GREEN
	_WHITE = color.Fore.WHITE
	_NONE = color.Style.RESET_ALL
	
	appName = os.path.splitext(os.path.basename(__file__))[0]
	
	def run_shell(logFiles, *args, **kwargs):
	    """
	    This runs the main controll loop calls subprocess, decodes the response and writes it to 
	    chattymoe.apps.shelly.currentTimeStamp out.log, psHist.log
	    sources:
	    from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
	    """
	    # define prompt strings like C:/temp>
	    ps, nPs = f"{os.getcwd()}> ", f"{os.getcwd()}> "
	    stdout, counter = [], 0
	    # main controll loop for the shell
	    while True:
	        urs = get_ur(ps, logFiles, *args, **kwargs)
	        for ur in urs.split('&&'):
	            # print(f"{ur = }")
	            ps = nPs
	            # from tabulate import tabulate as tb
	            ur, nPs = analyse_ur(  logFiles, ur, ps )
	            if not check_action(ur, nPs, logFiles, *args, **kwargs): continue
	            cmds = sts.apps[appName]['source'] + shlex.split(ur)
	            # takes cmds and runs them as a powershell command
	            out = subprocess.Popen( cmds,
	                                    shell=True,
	                                    stdout=subprocess.PIPE,
	                                    stderr=subprocess.STDOUT,
	                                    cwd=ps[:-2]
	                                    )
	            resp = decode_response(out, nPs, *args, **kwargs)
	            # print(f"\t {ps[:-2]}> {resp = }")
	            actionStr = f"{ps} {ur}\n{resp}\n{nPs}|\n"
	            print_cmds(ps, ur, cmds, actionStr, *args, **kwargs)
	        with open(logFiles['outLogPath'], "w") as f: f.write(f"\n{resp}\n{nPs}|\n") 
	        with open(logFiles['psLogPath'], "a") as f: f.write(actionStr)
	        time.sleep(5)
	
	def print_cmds(ps, ur, cmds, actionStr, *args, **kwargs):
	    print(f"{_WHITE}\n\tshelly.run_shell processing ...:")
	    shellIn = {
	                'set_shell_in': [f'{ps[:-2]}> {ur}'], 
	                'subprocess_cmd': cmds,
	                'subprocess_out': hlp.insert_newline(actionStr, *args, **kwargs),
	                }
	    # print(shellIn)
	    shellIn = tb(shellIn, headers='keys', tablefmt='github')
	    for line in shellIn.split('\n'):  print(f"\t\t{_CYAN}", line, f"{_NONE}")
	
	def decode_response(out, nPs, *args, **kwargs):
	    check = False
	    for i, enc in enumerate(sts.encodings):
	        try:
	            resp = out.stdout.read().decode(enc)
	            check = True
	            if not resp: continue
	            return resp.replace('\n\n', '')
	        except Exception as e:
	            print(f"{_YELLOW}\tshelly.run_shell: decoding error! {i}: {e}{_NONE}")
	            continue
	    print(f"{_CYAN}shelly.run_shell: decoding failed! setting nPs: {nPs}{_NONE}")
	    return nPs
	
	def check_action(ur, path, logFiles, *args, cwd, **kwargs):
	    # cwd = sts.psTestPath if cwd is None else cwd
	    if not path.replace(os.sep, '/').startswith(cwd):
	        msg = f"Permission denied to path '{path}'! You have only permissions for '{cwd}'!\n"
	        with open(logFiles['outLogPath'], "w") as f: f.write(msg)
	        with open(logFiles['psLogPath'], "a") as f: f.write(msg)
	        return False
	    else:
	        pass
	    if len(ur) > sts.psMaxLen:
	        msg = f"ERROR: Command '{ur}' too long! Max length is {sts.psMaxLen} characters!\n"
	        with open(logFiles['outLogPath'], "w") as f: f.write(msg)
	        with open(logFiles['psLogPath'], "a") as f: f.write(msg)
	        return False
	    return True
	
	def get_ur(ps, logFiles, *args, role, **kwargs):
	    """
	    gets the user input
	    This can be either by asking for input or by reading the in.log file
	    """
	    if role == 'user':
	        ur = input(ps).strip()
	    elif role == 'system':
	        ur, cnt = '', 0
	        while not ur:
	            if cnt != 0 and cnt % 10 == 0:
	                print(f"shelly.get_ur: Ready for user input ... {cnt} secs")
	            # read system/user input from file
	            with open(logFiles['inLogPath'], 'r') as f:
	                ur = f.read().strip()
	            time.sleep(1)
	            cnt += 1
	        with open(logFiles['inLogPath'], 'w') as f: f.write('')
	    # this replace is very unfortunate and due to openai constantly chaining commands
	    # even if beeing told not to do so
	    # currently I have no easy solution for this because & and ; might legitimately be used
	    # in some particular context
	    ur = ur.replace('&', '&&').replace(';', '&&')
	    return ur
	
	def write_log_file(filePath, outStr):
	    """
	    writes a string to a file
	    to be used from an outside application like chattymoe.chattymoe.py
	    """
	    with open(filePath, 'a') as f:
	        # f.truncate()
	        f.write('\n' + outStr)
	
	def analyse_ur(logFiles, ur, ps):
	    """
	    analyses the user input and returns the new prompt string
	    NOTE: some commands like cd require changes to class attributes
	        For example the current working directory must be part of the prompt string
	    """
	    # cwd = ps.strip()[:-1]
	    ur = ur.strip()
	    new_cwd = None
	    if ur == 'quit':
	        os.remove(logFiles['prcLogPath'])
	        exit()
	    elif ur.startswith('cd'):
	        os.chdir(ps[:-2])
	        new_cwd = os.path.abspath(ur.split()[1]).replace('\\', '/')
	        ur = f"cd {new_cwd}"
	        print('analyse_ur:', new_cwd, ur)
	    elif os.sep in ur:
	        ur = ur.replace(os.sep, '/')
	    else:
	        with open(logFiles['psLogPath'], 'r') as f:
	            lines = f.read().split('\n')
	            lines = lines[:-1]
	        with open(logFiles['psLogPath'], 'w') as f:
	            f.write('\n'.join(lines))
	    return ur, f"{new_cwd}> " if new_cwd is not None else ps
	
	def get_shell_response(logFiles, *args, **kwargs):
	    """
	    subprocess outpout/return has been written by an arbitrary process/sender from outside
	    this module to chattymoe.apps.shelly.currentTimeStamp.out.log
	    this output is read here
	    """
	    resp, cnt = '', 0
	    while not resp:
	        if cnt != 0 and cnt % 10 == 0:
	            print(f"Waiting for resp... {cnt} secs")
	        with open(logFiles['outLogPath'], 'r') as f:
	            resp = f.read().strip()
	        time.sleep(1)
	        cnt += 1
	    return resp
	
	def set_shell_in(logFiles, userInput, *args, **kwargs):
	    """
	    all commands can be passed to shellies subprocess by a in.log file
	    this funciton writes whatever is in userInput to in.log
	    shelly latter reads in.log and passes the content to the subprocess
	    """
	    # print(f"Writing to in.log: {userInput}")
	    with open(logFiles['inLogPath'], 'w') as f:
	        f.write(userInput)
	
	def mk_log_names(*args, **kwargs):
	    """
	    Creates the log names for directory and files
	    """
	    logDir = os.path.join(sts.appsDir, appName, f"{re.sub(r'([: .])', r'-' , str(dt.now()))}")
	    logFiles = {
	                'psLogPath': os.path.join(logDir, f"{sts.psHistFileName}"),
	                'inLogPath': os.path.join(logDir, f"in.log"),
	                'outLogPath': os.path.join(logDir, f"out.log"),
	                'prcLogPath': sts.prcLogPath,
	                }
	    return logDir, logFiles
	
	def mk_log_files(logDir, logFiles, *args, cwd=None, **kwargs):
	    """
	    Every chat creates a log folder in which in.log, out.log and psHist.log is stored
	    check chattymoe.apps.shelly.currentTimeStamp
	    """
	    os.mkdir(logDir)
	    for k, logFilePath in logFiles.items():
	        start = ''
	        if k == 'prcLogPath': continue
	        if k == 'inLogPath': start = f'cd {cwd}'
	        with open(logFilePath, 'w') as f: f.write(start)
	
	def setup_process(entryPoint, *args, **kwargs):
	    if entryPoint == 'run_shell':
	        logDir, logFiles = mk_log_names(*args, **kwargs)
	        mk_log_files(logDir, logFiles, *args, **kwargs)
	        with open(sts.prcLogPath, 'w') as f: f.write(yaml.dump(logFiles))
	    elif not os.path.exists(sts.prcLogPath):
	        return False
	    # logfiles are returned to be used with all processes (kind of shared memory)
	    with open(sts.prcLogPath, 'r') as f:
	        return yaml.safe_load(f)
	
	def main(*args, entryPoint=None, **kwargs):
	    # setup for the processes to run such as workFiles and params
	    entryPoint = 'run_shell' if entryPoint is None else entryPoint
	    logFiles = setup_process(entryPoint, *args, **kwargs)
	    if not logFiles: return f"shelly not running"
	    # entryPoint must be a funciton from this module, which is run now
	    out = getattr(sys.modules[__name__], entryPoint)(logFiles, *args, **kwargs)
	    # process.yml file indicates running process, hence is removed when process stops
	    if os.path.exists(logFiles['prcLogPath']) and entryPoint == 'run_shell':
	        os.remove(logFiles['prcLogPath'])
	    return out
	
	if __name__ == "__main__":
	    """
	    runns this shell emulator as a subprocess
	    creates a chat protcol chattymoe.apps.shelly.currentTimeStamp folder
	    shell commands can be entered into chattymoe.apps.shelly.currentTimeStamp -> in.log
	    Save the file to run the command!
	    
	    NOTE: type quit into in.log to end the program
	    """
	    # python .\chattymoe\apps/shelly/shelly.py
	    main(entryPoint='run_shell', role='system', cwd='C:/temp')
	
```

################### general.py ###################
```python
# general.py
	
	def insert_newline(text, maxLen=5, *args, **kwargs):
	    """
	    inserts a newline after every maxLen words
	    Example: If a text is longer than n words, it will be split into n / maxLen lines.
	    """
	    numWords = len(text.split())
	    if numWords <= maxLen:
	        return [text]
	    else:
	        newText, line = [], ''
	        for i, word in enumerate(text.split(), 1):
	            line += f"{word} "
	            if i % maxLen == 0 and i != 0:
	                # print('\t', line)
	                newText.append(line)
	                line = ''
	        return newText
```

############# markddown_to_python.py #############
```python
# markddown_to_python.py
	import os
	import re
	from datetime import datetime as dt
	"""
	takes a markdown file containing python documentation and converts it
	    to a python file with the same name and a .py extension.
	    """
	
	def load_file(filePath, *args, **kwargs):
	    """ 
	    load a file and return its contents as a string
	    """
	    with open(filePath, "r") as f:
	        return f.read()
	
	
	def make_file_names(filePath, pythonDir, *args, **kwargs):
	    """
	    takes the baseName of a filePath to a .md file and changes the file extension to .py
	    returns the full filePath to the .md file and the full filePath to the .py file
	    """
	    if filePath.endswith(".md"):
	        mdFilePath = filePath
	        pyFilePath = os.path.join(pythonDir, os.path.basename(filePath).replace(".md", ".py"))
	    elif filePath.endswith(".py"):
	        pyFilePath = filePath
	        mdFilePath = os.path.join(pythonDir, os.path.basename(filePath).replace(".py", ".md"))
	    return mdFilePath, pyFilePath
	
	def convert_markdown_to_python(mdText, *args, **kwargs):
	    """
	    takes the text from a markdown file and modifies it, so it can be saved as a python file
	    i.e. the python code sits inside tripple backticks which must be removed
	    i.e. the markdown file contains regular paragraphs which must be commented out
	    """
	    codeBlockStart, codeBlockEnd, isCodeBlock = "```python", "```", False
	    subs, replacer = [r'^[A-za-z0-9]'], "# <md>"
	    lines = []
	    for i, line in enumerate(mdText.split('\n')):
	        if i == 0:
	            line = line + f" Generated: {re.sub(r'([: .])', r'-' , str(dt.now()))}"
	        if line.startswith(codeBlockStart):
	            isCodeBlock = True
	            line = replacer + line
	        elif line.startswith(codeBlockEnd):
	            isCodeBlock = False
	            line = replacer + line
	        if isCodeBlock:
	            pass  
	        else:
	            if re.search(subs[0], line) and not line.startswith("#"):
	                line = replacer + line
	        lines.append(line)
	    return '\n'.join(lines)
	
	def convert_python_to_markdown(pyText, *args, **kwargs):
	    """
	    takes the text from a python file and modifies it, so it can be saved as a markdown file
	    reverses the effect of convert_markdown_to_python function above
	    NOTE: This function assumes, that the pyhton file was generated by the 
	    convert_markdown_to_python function above or folows the same format conventions.
	    """
	    lines, replacer = [], "# <md>"
	    for i, line in enumerate(pyText.split('\n')):
	        if i == 0:
	            line, _ = line.split(" Generated:")
	        if line.startswith(replacer):
	            line = line.replace(replacer, "")
	        lines.append(line)
	    return '\n'.join(lines)
	
	
	def save_to_file(filePath, fileContent, *args, **kwargs):
	    """ 
	    save a string to a file
	    """
	    with open(filePath, "w") as f:
	        f.write(fileContent)
```

################## test_chat.py ##################
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	from chattymoe.actions import chat
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        # cls.testData = cls.load_test_data(*args, **kwargs)
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    def load_test_data(cls, fileName, *args, **kwargs):
	        with open(os.path.join(sts.testDataDir, fileName), "r") as f:
	            out = yaml.safe_load(f)
	        return out
	
	    def test_comunicate(*args, **kwargs):
	        lang = 'en'
	        text = 'This is a test' if lang == 'en' else 'Dies ist ein Test'
	        chat.communicate(text, *args, lang=lang, origin='audio', verbose=1,  **kwargs)
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

############### test_chattymoe.py ################
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	from chattymoe.chattymoe import Moe as PC
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        cls.testData = cls.mk_test_data(*args, **kwargs)
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    @classmethod
	    def mk_test_data(cls, *args, **kwargs):
	        with open(os.path.join(sts.testDataPath, "chattymoe.yml"), "r") as f:
	            out = yaml.safe_load(f)
	        return out
	
	    def test__str__(self, *args, **kwargs):
	        kwargs.update(self.testData)
	
	        expected = (
	            f"chattymoe.chattymoe.py"
	        )
	        pc = PC(*args, **kwargs)
	        self.assertEqual(pc.__str__(*args, *kwargs), expected)
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

################ test_content.py #################
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	from chattymoe.content import Content as PC
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        # cls.testData = cls.load_test_data(*args, **kwargs)
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    def load_test_data(cls, fileName, *args, **kwargs):
	        with open(os.path.join(sts.testDataDir, fileName), "r") as f:
	            out = yaml.safe_load(f)
	        return out
	
	    def test_get_text(self, *args, **kwargs):
	        expected = '## Your Identy:'
	        testData = self.load_test_data('test_content.yml')
	        ti = PC(*args, origin=None, **kwargs)
	        out = ti.get_text(*args, content=testData[0].get('content'), **kwargs)
	        self.assertTrue(out.strip().startswith(expected))
	        # test from_stdout
	        expected = 'Not implemented yet!'
	        ti = PC(*args, origin='system', **kwargs)
	        out = ti.get_text(*args, content=testData[0].get('content'), **kwargs)
	        self.assertTrue(out.strip().startswith(expected))
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

########### test_markdown_to_pyhton.py ###########
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	import chattymoe.helpers.markddown_to_python as test_module
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        # cls.testData = cls.mk_test_data(*args, **kwargs)
	        cls.mdFilePath = os.path.join(sts.testDataDir, "test_markdown_to_python_testfile.md")
	        cls.pyFilePath = os.path.join(sts.testDataDir, "test_markdown_to_python_testfile.py")
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    # @classmethod
	    # def mk_test_data(cls, *args, **kwargs):
	    #     with open(os.path.join(sts.testDataDir, "response.txt"), "r") as f:
	    #         out = f.read()
	    #     return out
	
	    def test_make_file_names(self, *args, **kwargs):
	        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
	        expected = os.path.join(sts.testDataDir, self.pyFilePath)
	        mdFilePath, pyFilePath = test_module.make_file_names(
	                                                                filePath, 
	                                                                sts.testDataDir,
	                                                                *args, **kwargs
	                                                                )
	        self.assertEqual(pyFilePath, expected)
	
	    def test_load_file(self, *args, **kwargs):
	        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
	        expected = "# Test of Python and Markdown in one file"
	        mdText = test_module.load_file(filePath, *args, **kwargs)
	        self.assertEqual(mdText[:len(expected)], expected)
	
	    def test_convert_markdown_to_python(self, *args, **kwargs):
	        expected = '# <md>General imports'
	        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
	        mdText = test_module.load_file(filePath, *args, **kwargs)
	        converted = test_module.convert_markdown_to_python(mdText, *args, **kwargs)
	        self.assertTrue(expected in converted)
	
	    def test_save_to_file(self, *args, **kwargs):
	        filePath = os.path.join(sts.testDataDir, self.mdFilePath)
	        mdFilePath, pyFilePath = test_module.make_file_names(
	                                                                filePath, 
	                                                                sts.testDataDir,
	                                                                *args, **kwargs
	                                                                )
	        mdText = test_module.load_file(mdFilePath, *args, **kwargs)
	        converted = test_module.convert_markdown_to_python(mdText, *args, **kwargs)
	        test_module.save_to_file(pyFilePath, converted, *args, **kwargs)
	        from chattymoe.test.data.test_markdown_to_python_testfile import ping
	        self.assertEqual(ping(), "pong")
	
	    def test_convert_python_to_markdown(self, *args, **kwargs):
	        time.sleep(.5)
	        filePath = os.path.join(sts.testDataDir, self.pyFilePath)
	        mdFilePath, pyFilePath = test_module.make_file_names(
	                                                                filePath, 
	                                                                sts.testDataDir,
	                                                                *args, **kwargs
	                                                                )
	        pyText = test_module.load_file(pyFilePath, *args, **kwargs)
	        converted = test_module.convert_python_to_markdown(pyText, *args, **kwargs)
	        mdText = test_module.load_file(mdFilePath, *args, **kwargs)
	        self.assertEqual(converted, mdText)
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

################# test_prompt.py #################
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	from chattymoe.prompt import Prompt as PC
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        # cls.testData = cls.load_test_data(*args, **kwargs)
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    def load_test_data(cls, fileName, *args, **kwargs):
	        with open(os.path.join(sts.testDataDir, fileName), "r") as f:
	            out = yaml.safe_load(f)
	        return out
	
	    def test_handle_contents(self, *args, **kwargs):
	        in_entry = {'content': '', 'meta': [None, 0], 'role': ''}
	        expected = {'content': 'Hello there!', 'meta': [None, 0], 'role': ''}
	        ti = PC(*args, **kwargs)
	        entry = ti.handle_contents(in_entry, *args, **kwargs)
	        self.assertEqual(entry, expected)
	        # test_from_stdout
	        expected = {'content': 'Not implemented yet!', 'meta': [None, 0], 'role': ''}
	        ti = PC(*args, **kwargs)
	        entry = ti.handle_contents(in_entry, *args, origin='system', running=True, **kwargs)
	        self.assertEqual(entry, expected)
	
	    def test_create_prompt(self, *args, **kwargs):
	        expected = {'content': 'Hello there!', 'meta': [None, 0], 'role': 'system'}
	        ti = PC(*args, **kwargs)
	        entry = ti.create_prompt(*args, verbose=0, origin='system', **kwargs)
	        self.assertEqual(entry, expected)
	        # test_from_stdout
	        expected = {'content': 'Not implemented yet!', 'meta': [None, 0], 'role': 'system'}
	        ti = PC(*args, **kwargs)
	        entry = ti.create_prompt(*args,  verbose=0, origin='system', running=True, **kwargs)
	        self.assertEqual(entry, expected)
	        # test_from_stdout
	        text = self.load_test_data('test_content.yml')[-1].get('content')
	        expected = {'content': text.replace('<colon>', ': '), 'meta': [None, 0], 'role': 'system'}
	        ti = PC(*args, **kwargs)
	        entry = ti.create_prompt(*args, content=text, verbose=0, origin='system', running=True, **kwargs)
	        # print(entry)
	        self.assertEqual(entry, expected)
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

################ test_response.py ################
```python
# standard lib imports
	import colorama as color
	
	color.init()
	
	import os, re, shutil, sys, time
	import yaml
	import unittest
	
	# test package imports
	import chattymoe.settings as sts
	from chattymoe.response import Response as TC
	
	
	# print(f"\n__file__: {__file__}")
	
	
	class UnitTest(unittest.TestCase):
	    @classmethod
	    def setUpClass(cls, *args, **kwargs):
	        cls.verbose = 0
	        cls.testData = cls.mk_test_data(*args, **kwargs)
	
	    @classmethod
	    def tearDownClass(cls, *args, **kwargs):
	        pass
	
	    @classmethod
	    def mk_test_data(cls, *args, **kwargs):
	        with open(os.path.join(sts.testDataPath, "response.txt"), "r") as f:
	            out = f.read()
	        return out
	
	    def test_clean_response(self, *args, **kwargs):
	        start, end = "Get-ChildItem", "}"
	        ti = TC(self.testData, *args, **kwargs)
	        out = ti.clean_response(*args, *kwargs)
	        self.assertTrue(out.startswith(start) and out.endswith(end))
	
	
	if __name__ == "__main__":
	    unittest.main()
	    print("done")
	    exit()
	
```

################## __init__.py ###################
```python

```

###### test_markdown_to_python_testfile.py #######
```python
# Test of Python and Markdown in one file Generated: 2023-04-03-18-01-05-263200
	
	# <md>General imports
	
	# <md>```python
	import os
	# <md>```` 
	
	# <md>This is a test of python and markdown in one file
	# <md>```python
	
	def ping(*args, **kwargs):
	    """
	    returns pong
	    """
	    for i in range(1):
	        pass
	    return f"pong"
	# <md>```
	
	# <md>Lets run the code
	
	# <md>```python
	if __name__ == '__main__':
	    ping()
	# <md>```` 
	
	# End of Test of Python and Markdown in one file
```

</chatgpt>
