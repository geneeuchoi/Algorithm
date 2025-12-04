from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def recursive(n):
	dp = [0] * (n+1)
	dp[1], dp[2] = 1, 1

	for i in range(3, n+1):
	    dp[i] = dp[i-1] + dp[i-2]

	return dp[n]

def dp(n):
    return n-2

n = int(stdin.readline().rstrip())
step = 0
print(recursive(n), dp(n))