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