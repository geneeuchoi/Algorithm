import sys

N = int(sys.stdin.readline())
intList = list(map(int, sys.stdin.readline().split(' ')))
v = int(sys.stdin.readline())

vCnt = 0

for i in intList:
    if i == v:
        vCnt += 1

print(vCnt)