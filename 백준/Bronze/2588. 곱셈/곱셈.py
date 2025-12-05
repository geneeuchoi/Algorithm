from sys import stdin, setrecursionlimit

n1 = int(stdin.readline().rstrip())
n2 = stdin.readline().rstrip()

for i in range(2, -1, -1):
	print(n1 * int(n2[i]))
print(n1*int(n2))