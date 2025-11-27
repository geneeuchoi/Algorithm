from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(" "))
N_list, include = [], 0

for _ in range(N):
    N_list.append(stdin.readline().rstrip())

for _ in range(M):
    tmp = stdin.readline().rstrip()
    if tmp in N_list: include += 1

print(include)