from sys import stdin, setrecursionlimit


n = int(stdin.readline().rstrip())
sequence = list(map(int, stdin.readline().rstrip().split(" ")))

ascend_dp = [1 for _ in range(n)]
descend_dp = [1 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(0, n):
	for j in range(i):
		if sequence[i] > sequence[j]:
			ascend_dp[i] = max(ascend_dp[i], ascend_dp[j]+1)


for i in range(n-1, -1, -1):
	for j in range(n-1, i, -1):
		if sequence[i] > sequence[j]:
			descend_dp[i] = max(descend_dp[i], descend_dp[j]+1)

for i in range(n):
	dp[i] = ascend_dp[i] + descend_dp[i] - 1

print(max(dp))