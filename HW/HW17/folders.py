import re
import os
import shutil

filename = []
unique = []
name = ''

def numberinf():
    number = 0
    for f in os.listdir('REALEC'):
        name = str(f)
        b = re.sub(r'\.\D+', '', name)
        c = re.search(r'\d', b)
        if c != None:
            number += 1
    return number

def foldername():
    for f in os.listdir('REALEC'):
        name = str(f)
        b = re.sub(r'\.\D+', '', name)
        filename.append(b)
    for n in filename:
        if n != '' and n not in unique:
            unique.append(n)
    return unique

print(numberinf(), foldername())
