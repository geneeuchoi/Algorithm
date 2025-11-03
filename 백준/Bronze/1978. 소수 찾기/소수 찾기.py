import sys
from sys import stdin

def prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip().split(" ")))
result = 0

for num in nums:
    if prime(num) and num != 1: result += 1

print(result)