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
