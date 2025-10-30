import sys
from sys import stdin
T = int(stdin.readline().strip())
for _ in range(T):
    h, w, n = map(int, stdin.readline().strip().split(" "))
    cnt = 0
    for room in range(1, w+1):
        for floor in range(1, h+1):
            cnt += 1
            if cnt == n:
                if room < 10: print(f'{floor}0{room}')
                else: print(f'{floor}{room}')
                break