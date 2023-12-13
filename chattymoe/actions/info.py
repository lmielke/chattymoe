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
