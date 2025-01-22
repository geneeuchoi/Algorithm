import sys

N, M = sys.stdin.readline().rstrip().split(' ')
N, M = int(N[::-1]), int(M[::-1])

if N > M:
    print(N)
else:
    print(M)