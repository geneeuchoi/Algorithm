import sys
from sys import stdin

def factorial(n):
    sum_fac = 1
    for i in range(2, n+1):
        sum_fac *= i
    return sum_fac

N, K = map(int, stdin.readline().rstrip().split(" "))
if N == 1: print(1)
else: print(int(factorial(N)/(factorial(K)*factorial(N-K))))
