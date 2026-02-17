from sys import stdin

n = int(stdin.readline().rstrip())
dp = [1 for _ in range(n)]
if n == 1:
	print(dp[n-1])
	exit()

dp[0], dp[1] = 1, 2
for i in range(2, n):
	dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1]%10007)
