from sys import stdin, setrecursionlimit

n = int(stdin.readline().rstrip())
dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1인 수는 모두 1가지 경우만 있음
for j in range(1, 10):
    dp[1][j] = 1

# i = 수의 길이
# 길이가 2인 수부터 n인 수까지
for i in range(2, n + 1):
	# j = 마지막 숫자
    for j in range(10):
        # 마지막 숫자가 0인 경우: 앞에 무조건 1이 와야 함
        if j == 0:
            dp[i][j] = dp[i-1][1]
        
        # 마지막 숫자가 9인 경우: 앞에 무조건 8이 와야 함
        elif j == 9:
            dp[i][j] = dp[i-1][8]
            
        # 그 외 (1~8): 앞자리가 j-1 또는 j+1 가능
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            
print(sum(dp[n]) % 1000000000)
