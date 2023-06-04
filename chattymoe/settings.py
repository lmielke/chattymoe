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