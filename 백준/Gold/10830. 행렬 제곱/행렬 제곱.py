from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def first_matrix(n):
	matrix = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		matrix[i][i] = 1
	return matrix
	
def matrix(prev1, prev2):
	new_prev = []
	for i in range(n):
		tmp = []
		for j in range(n):
			elem = 0
			for l in range(n):
				elem += (prev1[i][l] * prev2[l][j])
			tmp.append(elem%1000)
		new_prev.append(tmp)
	return new_prev


def recursive(b):
	if b == 0: return first_matrix(n)
	x = recursive(b//2)
	val = matrix(x, x)
	if b % 2 == 0: return val
	else: return matrix(val, a)

n, b = map(int, stdin.readline().rstrip().split(" "))
a = []
for _ in range(n):
	a.append(list(map(int, stdin.readline().rstrip().split(" "))))

answer = recursive(b)
for i in range(n):
	for j in range(n):
		print(answer[i][j], end = " ")
	print()



