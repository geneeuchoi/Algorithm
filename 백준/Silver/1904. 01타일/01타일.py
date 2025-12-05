from sys import stdin, setrecursionlimit

n = int(stdin.readline().rstrip())

if n == 1:
	print(1)
	exit()

if n == 2:
	print(2)
	exit()

dp = [1, 2]

for i in range(2, n):
	val = (dp[i-2] + dp[i-1]) % 15746
	dp.append(val)

print(dp[n-1])