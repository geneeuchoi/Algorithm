from sys import stdin, setrecursionlimit

def find(n):
	dp = [1, 1, 1] + [0 for _ in range(n-3)]
	for i in range(3, n):
		dp[i] = dp[i-2] + dp[i-3]

	return dp[n-1]

t = int(stdin.readline().rstrip())
for _ in range(t):
	n = int(stdin.readline().rstrip())
	print(find(n))
