import sys
from sys import stdin

melody = list(map(int, stdin.readline().strip().split(" ")))
up_flag, down_flag = True, True
for i in range(len(melody)-1):
    if melody[i+1] != melody[i]+1: 
        up_flag = False
    if melody[i+1] != melody[i]-1:        
        down_flag = False
        
if up_flag: print("ascending")
elif down_flag: print("descending")
else: print("mixed")