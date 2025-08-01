from sys import stdin

N, M = map(int, stdin.readline().strip().split(' '))
A = list(map(int, stdin.readline().strip().split(' ')))
B = list(map(int, stdin.readline().strip().split(' ')))

A.sort()
B.sort()

combined = A + B
combined.sort()

for elem in combined:
    print(elem, end = ' ')