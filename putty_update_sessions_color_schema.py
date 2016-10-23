import csv
from easyprocess import EasyProcess
import os
import re
import sys

# run first
# regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham

file_in = "putty_dos2unix.reg"
file_ou = "putty_updated.reg"

colour_map = {
    "Colour0": "255,255,255",
    "Colour1": "255,255,255",
    "Colour2": "0,0,0",
    "Colour3": "85,85,85",
    "Colour4": "0,0,0",
    "Colour5": "0,255,0",
    "Colour6": "0,0,0",
    "Colour7": "85,85,85",
    "Colour8": "255,128,255",
    "Colour9": "255,128,255",
    "Colour10": "128,255,128",
    "Colour11": "85,255,85",
    "Colour12": "255,255,128",
    "Colour13": "255,255,85",
    "Colour14": "128,255,255",
    "Colour15": "128,255,255",
    "Colour16": "128,128,255",
    "Colour17": "255,85,255",
    "Colour18": "0,187,187",
    "Colour19": "85,255,255",
    "Colour20": "187,187,187",
    "Colour21": "255,255,255",
}

def main():
    fout = open(file_ou, 'w')
    with open(file_in) as fin:
        content = fin.readlines()
        for line in content:
            if line.startswith('"Colour'):
                ret = line.split('"')
                color_tag = ret[1]
                line = '"{}"="{}"\n'.format(color_tag, colour_map[color_tag])
            fout.write(line)

    fout.close()  # you can omit in most cases as the destructor will call it


if __name__ == '__main__':
    sys.exit(main())