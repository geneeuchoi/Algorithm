import sys
from sys import stdin

T = int(stdin.readline().strip())
for _ in range(T):
    result = stdin.readline().strip()
    score, cnt = 0, 0
    for i in range(len(result)):
        if result[i] == 'O': 
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)

