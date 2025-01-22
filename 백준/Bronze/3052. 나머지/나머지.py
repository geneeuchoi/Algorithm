import sys

namList = []
differentNumCnt = 0

for _ in range(10):
    i = int(sys.stdin.readline())
    if i % 42 in namList:
        differentNumCnt += 1
    namList.append(i % 42)

print(10-differentNumCnt)