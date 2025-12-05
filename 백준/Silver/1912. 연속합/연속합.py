from sys import stdin, setrecursionlimit

n = int(stdin.readline().rstrip())
n_arr = list(map(int, stdin.readline().rstrip().split(" ")))

dp = [0] * n
dp[0] = n_arr[0]

for i in range(1, n):
    dp[i] = max(n_arr[i], dp[i-1] + n_arr[i])

print(max(dp))