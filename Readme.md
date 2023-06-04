# Readme

<img src="https://drive.google.com/uc?id=1C8LBRduuHTgN8tWDqna_eH5lvqhTUQR4" alt="me_happy" class="plain" height="150px" width="220px">

## ChattyMoe
NOTE: This is a terrible prototype and not ready for use. It is currently in development.
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

```
    moe info
    moe $action -a $application -v $verbose -y -r # -r for un-modified raw content
    moe 'how to list files from current directory' -a powershell -v 2 -y

    # be extra careful when running
    moe auto -a shelly -c auto_python [-y]
```

## install
- check and or update Pipfile/requirements.txt
- RUN: pipenv install [-d] NOTE: some dev packages are not available to you, so run without -d
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
