import sys
from sys import stdin

M, N = map(int, stdin.readline().rstrip().split(" "))
if M == 1: M += 1
prime = [True] * (N+1)
prime[0], prime[1] = False, False

for i in range(2, N//2+1):
    if prime[i]:
        for j in range(i*i, N+1, i):
            prime[j] = False

for i in range(M, len(prime)):
    if prime[i]: print(i)