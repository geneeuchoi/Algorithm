import sys

N, L = map(int, sys.stdin.readline().rstrip().split(' '))
places = list(map(int, sys.stdin.readline().rstrip().split(' ')))
places.sort()

cnt = 1
start = places[0] - 0.5

for i in range(1, N):
    if places[i] + 0.5 > start + L:
        start = places[i] - 0.5
        cnt += 1

print(cnt)
