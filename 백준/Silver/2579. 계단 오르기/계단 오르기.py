from sys import stdin, setrecursionlimit

def sol():
    if n == 0: return 0
    if n == 1: return floor[0]
    if n == 2: return floor[0] + floor[1]
    
    dp[0] = floor[0]
    dp[1] = floor[0] + floor[1]
    dp[2] = max(floor[0] + floor[2], floor[1] + floor[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + floor[i-1]) + floor[i]

    return dp[n-1]

n = int(stdin.readline().rstrip())
floor = []
dp = [0] * 301

for _ in range(n):
	floor.append(int(stdin.readline().rstrip()))

print(sol())