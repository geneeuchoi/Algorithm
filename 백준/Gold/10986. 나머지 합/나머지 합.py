from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

n, m = map(int, stdin.readline().rstrip().split(" "))
a = list(map(int, stdin.readline().rstrip().split(" ")))
dp = [1] + [0 for _ in range(m-1)]
idx = 0

for x in a:
	idx = (idx + x) % m
	dp[idx] += 1


cnt = 0
for idx in dp:
	if idx >= 2:
		cnt += idx * (idx - 1) // 2

print(cnt)