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