# shelly.py
"""
python ./chattymoe/apps/shelly/shelly.py
NOTE: to stop type quit in chattymoe.apps.shelly.in.log
"""

import subprocess
import os, re, shlex, sys, time, yaml
from datetime import datetime as dt
import chattymoe.settings as sts

import colorama as color

color.init()
_RED = color.Fore.RED
_CYAN = color.Fore.CYAN
_YELLOW = color.Fore.YELLOW
_GREEN = color.Fore.GREEN
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
            print(f"{ur = }")
            ps = nPs
            ur, nPs = analyse_ur(  logFiles, ur, ps )
            if not check_action(ur, nPs, logFiles, *args, **kwargs): continue
            print(f"{_CYAN}\nshelly.run_shell.subprocess:{_NONE}")
            cmds = sts.apps[appName]['source'] + shlex.split(ur)
            print(f"\t {ps[:-2]}> {ur}   ->   {cmds = }")
            # takes cmds and runs them as a powershell command
            out = subprocess.Popen( cmds,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    cwd=ps[:-2]
                                    )
            resp = decode_response(out, nPs, *args, **kwargs)
            print(f"\t {ps[:-2]}> {resp = }")
            actionStr = f"{ps} {ur}\n{resp}\n{nPs}|\n"
            with open(logFiles['outLogPath'], "w") as f: f.write(f"\n{resp}\n{nPs}|\n") 
            with open(logFiles['psLogPath'], "a") as f: f.write(actionStr)
            time.sleep(5)

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
    print(f"Writing to in.log: {userInput}")
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
