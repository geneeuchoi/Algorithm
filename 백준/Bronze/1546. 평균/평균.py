import sys

N = int(sys.stdin.readline())
scoreList = list(map(int, sys.stdin.readline().split(' ')))
scoreList.sort()
M = scoreList[N-1]

sum = 0
for score in scoreList:
    sum += score / M * 100

print(sum / N)

