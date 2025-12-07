from sys import stdin, setrecursionlimit

def find():
	dp = [0 for _ in range(n+1)]
	
	if n == 1: return wines[1]
	if n == 2: return wines[1] + wines[2]
	
	dp[1] = wines[1]
	dp[2] = wines[1] + wines[2]

	for i in range(3, n + 1):
		dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])
	return dp[n]


n = int(stdin.readline().rstrip())
wines = [0]
for _ in range(n):
	wine = int(stdin.readline().rstrip())
	wines.append(wine)

print(find())