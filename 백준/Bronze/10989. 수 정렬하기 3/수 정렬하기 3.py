import sys

N = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(len(nums)):
    for j in range(nums[i]):
        print(i)