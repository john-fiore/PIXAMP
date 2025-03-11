# PIXAMP: Resolution Calculator
# Copyright © 2025 John Fiore,
# All Rights Reserved.
# ------------------------------
# NAME       : pixamp.py
# AUTH       : John Fiore
# DESC       : Main File
# CRTD       : 03/11/2025
# UPTD       : 03/11/2025

import global_funcs as gf
from colorama import Fore, Style, init # haha golf
import re

init(autoreset=True)

title = "PIXAMP"
color = [Fore.RED, Fore.GREEN, Fore.BLUE]

title_colored = "".join(color[z % 3] + letter for z, letter in enumerate(title))

def main():
    gf.clear()
    
    print(f"Welcome to {title_colored}!")
    print()
    multinp = input("What do you want to multiply by: ")
    
    while True:
        reso = input("What is your resolution (Include 'x', no spaces): ")
        
        # Validate the input
        if not re.fullmatch(r"\d+x\d+", reso):
            print(f"{Fore.RED}Error: Invalid resolution format. Use only numbers and 'x' (e.g., 1920x1080).{Style.RESET_ALL}")
            continue
        
        break
    
    mult = int(multinp)
    arg1, arg2 = map(int, reso.split("x"))

    farg1 = arg1 * mult
    farg2 = arg2 * mult

    print(f"Final Resolution: {farg1}x{farg2}")
    input()
    main()

if __name__ == "__main__":
    main()
