# info.py
import chattymoe.settings as sts
from chattymoe.chattymoe import Moe
import subprocess
import os, sys

import colorama as color

color.init()


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

def main(*args, **kwargs):
    ignoreDirs = {'.git', 'build', 'dist', 'logs', 'chattymoe.egg-info', '__pycache__'}
    project_structure = get_package_info(*args, **kwargs)
    projectDir = sts.projectDir
    project_structure += '\n## Project Structure\n'
    project_structure += f"projectDir: {projectDir}\n"
    project_structure += f"packageDir: {sts.packageDir}\n"
    project_structure += f"{generate_folder_tree(projectDir, ignoreDirs, *args, **kwargs)}\n"
    project_structure += f"ignoreDirs: {ignoreDirs}\n"
    return project_structure

if __name__ == '__main__':
    out = main()
    print(project_structure)
