import sys
from sys import stdin


T = int(stdin.readline().strip())
for _ in range(T):
    k = int(stdin.readline().strip())
    n = int(stdin.readline().strip())

    apt = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(n):
        apt[0][i] = i + 1

    for i in range(1, k+1):
        cnt = 0
        for j in range(n):
            cnt += apt[i-1][j]
            apt[i][j] = cnt
    print(apt[k][n-1])
