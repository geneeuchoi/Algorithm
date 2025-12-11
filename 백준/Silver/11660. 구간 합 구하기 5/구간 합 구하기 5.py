from sys import stdin, setrecursionlimit

# n 표의 크기
# 합을 구해야 하는 크기
n, m = map(int, stdin.readline().rstrip().split(" "))

array = []
for _ in range(n):
	tmp = list(map(int, stdin.readline().rstrip().split(" ")))
	array.append(tmp)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		val = array[i-1][j-1]
		dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + val

for _ in range(m):
	x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split(" "))
	answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
	print(answer)
