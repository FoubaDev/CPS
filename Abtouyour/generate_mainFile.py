#!/usr/bin/python3

import os

def generate_file(n):
    """
    Generates  files
    """
    for i in range(1,n):
        if os.path.exists("Abtouyour_"+str(i)+".xls"):
            pass
        else:
            with open(("Abtouyour_"+str(i)+".xls"), "w") as file:
                file.write(" ")
        
generate_file(26)
