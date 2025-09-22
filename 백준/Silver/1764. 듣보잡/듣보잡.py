from sys import stdin

N, M = map(int, stdin.readline().split())
see = set()
hear = set()

for _ in range(N):
	see.add(stdin.readline().strip())

for _ in range(M):
	hear.add(stdin.readline().strip())

see_hear = list(see.intersection(hear))
see_hear.sort()

print(len(see_hear))
for elem in see_hear:
	print(elem)