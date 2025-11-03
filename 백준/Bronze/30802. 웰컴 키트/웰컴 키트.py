import sys
from sys import stdin

N = int(stdin.readline().rstrip())
size = list(map(int, stdin.readline().rstrip().split(" ")))
T, P = map(int, stdin.readline().rstrip().split(" "))

result_t, result_p1, result_p2 = 0, 0, 0

for t in size:
    result_t += t // T
    if t % T != 0:
        result_t += 1

result_p1 = N // P
result_p2 = N % P

print(result_t)
print(result_p1, result_p2)
