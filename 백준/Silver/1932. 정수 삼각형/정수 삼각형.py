from sys import stdin, setrecursionlimit

def dp():
	# 합이 최대가 되는 경로에 있는 수의 합
	for i in range(1, n):
		floor_n = len(pyramid[i])
		for j in range(floor_n):
			if j == 0: pyramid[i][j] += pyramid[i-1][j]
			elif j == floor_n-1: pyramid[i][j] += pyramid[i-1][j-1]
			else: pyramid[i][j] += max(pyramid[i-1][j-1], pyramid[i-1][j])

	return max(pyramid[n-1])

n = int(stdin.readline().rstrip())
pyramid = []
for _ in range(n):
	pyramid.append(list(map(int, stdin.readline().rstrip().split(" "))))

print(dp())