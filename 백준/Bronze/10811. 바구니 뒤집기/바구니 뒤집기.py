import sys

N, M = map(int, sys.stdin.readline().split(' '))
bucket = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(' '))
    temp = bucket[i-1:j]
    temp.reverse()
    bucket[i-1:j] = temp

for elem in bucket:
    print(elem, end = " ")