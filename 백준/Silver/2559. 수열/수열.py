from sys import stdin, setrecursionlimit

n, k = map(int, stdin.readline().rstrip().split(" "))
temp = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = temp[0]
for i in range(1, n):
	dp[i] = dp[i-1] + temp[i]

answer = [dp[k-1]]+[]
for end in range(k, n):
	answer.append(dp[end]-dp[end-k])
print(max(answer))
	
