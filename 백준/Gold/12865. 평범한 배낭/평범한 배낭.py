from sys import stdin, setrecursionlimit

# 물품의 수 n
# 가방 가능 무게 k
# 물건 무게 w
# 물건 가치 v
n, k = map(int, stdin.readline().rstrip().split(" "))

stuff = [[0,0]] 
for _ in range(n):
    stuff.append(list(map(int, stdin.readline().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

# [물건 개수][가방의 가능한 무게]
# e.g. [3][7] = 7 물건 3개로 7kg 만들 수 있고, 그 가치는 7임.
# 이 물건을 못 넣을 경우에는 물건 하나 없고, 같은 무게인거 갖고옴
# 이 물건이나 이 전 물건을 조합해서 둘 중 큰 것을 dp 값으로 넣는다.

for i in range(1, n + 1): 
    weight = stuff[i][0]
    value = stuff[i][1]
    
    for j in range(1, k + 1): 
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)


print(dp[n][k])