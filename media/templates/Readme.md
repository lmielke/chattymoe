# Readme

<img src="https://drive.google.com/uc?id=1C8LBRduuHTgN8tWDqna_eH5lvqhTUQR4" alt="me_happy" class="plain" height="150px" width="220px">

## ChattyMoe
ChattyMoe is a python application that authonomously builds python applications. It uses the OpenAI API to generate project structurs and codes python modules. It is currently in development and not ready for use.

## Example:
moe 

## get and install
```
git clone git@gitlab.com:larsmielke2/chattymoe.git
```

### run in Shell
```
    moe $action -a $application -v $verbose -y -r # -r for un-modified raw content
    moe 'how to list files from current directory' -a powershell -v 2 -y
```

## install
- check and or update Pipfile/requirements.txt
- RUN: pipenv install -d
- add your openAi apiKey to chattymoe.settings.py or diretly to chattymoe.api_key.py -> get_api_key


## Project Structure
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
