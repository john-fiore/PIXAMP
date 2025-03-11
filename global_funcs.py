# PIXAMP: Resolution Calculator
# Copyright © 2025 John Fiore,
# All Rights Reserved.
# ------------------------------
# NAME       : global_funcs.py
# AUTH       : John Fiore
# DESC       : All global functions
# CRTD       : 03/11/2025
# UPTD       : 03/11/2025

import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")