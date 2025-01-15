import sys

T = int(sys.stdin.readline())

def fibonacci_count(n):
    dp = [(1, 0), (0, 1)] 
    for i in range(2, n + 1):
        zero_cnt = dp[i - 1][0] + dp[i - 2][0]
        one_cnt = dp[i - 1][1] + dp[i - 2][1]
        dp.append((zero_cnt, one_cnt))
    return dp[n]

for _ in range(T):
    N = int(sys.stdin.readline())
    zeroCnt, oneCnt = fibonacci_count(N)
    print(zeroCnt, oneCnt)
