import sys
from sys import stdin

while(True):
    word = stdin.readline().rstrip()
    if word == "0": exit()

    flag, length = True, len(word)

    for i in range(length//2):
        if word[i] != word[length-i-1]: flag = False

    if flag: print("yes")
    else: print("no")
