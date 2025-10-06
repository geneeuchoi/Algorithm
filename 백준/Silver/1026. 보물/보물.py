from sys import stdin

N = int(stdin.readline().strip())
A = list(map(int, stdin.readline().strip().split(' ')))
B = list(map(int, stdin.readline().strip().split(' ')))
S = 0

A.sort()
B.sort(reverse = True)

for i in range(N):
    S += A[i] * B[i]

print(S)