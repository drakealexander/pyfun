'''Utility library of ASCII art functions'''

from subprocess import check_output
import colors as c

def join(these,sep=""):
    joined = ""
    tjoin = [str(i).split("\n") for i in these]
    longest = 0
    for t in tjoin:
        l = len(t)
        if l > longest: longest = l
    for i in range(longest):
        for j in range(len(tjoin)):
            joined += tjoin[j][i] + sep
        joined += "\n"
    return joined

def hmargin(textlength):
    cols = int(check_output(['tput','cols']))
    return int((cols - textlength) / 2) - 1

def vmargin(linecount=1):
    rows = int(check_output(['tput','lines']))
    return int((rows - linecount)/2) - 1

def print_middle(text):
    hm = hmargin(len(text))
    vm = vmargin()
    print(c.clear + vm * '\n')
    print(" " * hm + text)
    print(vm * '\n')

