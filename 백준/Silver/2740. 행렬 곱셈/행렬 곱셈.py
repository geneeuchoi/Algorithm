from sys import stdin, setrecursionlimit

n, m = map(int, stdin.readline().rstrip().split(" "))
a = []
for _ in range(n):
	a.append(list(map(int, stdin.readline().rstrip().split(" "))))

m, k = map(int, stdin.readline().rstrip().split(" "))
b = []
for _ in range(m):
	b.append(list(map(int, stdin.readline().rstrip().split(" "))))

answer = []

for i in range(n):
	tmp = []
	for j in range(k):
		elem = 0
		for l in range(m):
			elem += a[i][l] * b[l][j]
		tmp.append(elem)
	answer.append(tmp)

for i in range(n):
	for j in range(k):
		print(answer[i][j], end = " ")
	print()