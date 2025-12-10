from sys import stdin, setrecursionlimit

# 수의 개수 n
# 테스트 케이스 m
n, m = map(int, stdin.readline().rstrip().split(" "))
nums = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = nums[0]
for i in range(1, n):
	dp[i] = dp[i-1] + nums[i]

for _ in range(m):
	i, j = map(int, stdin.readline().rstrip().split(" "))
	i -= 2
	j -= 1
	if i >= 0: print(dp[j] - dp[i])
	else: print(dp[j])
