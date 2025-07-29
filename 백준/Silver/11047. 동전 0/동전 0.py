import sys

N, K = map(int, sys.stdin.readline().strip().split(' '))
coin_list = []

for _ in range(N):
    coin = int(sys.stdin.readline().strip())
    if coin < K: 
        coin_list.append(coin)
    elif coin == K:
        print(1)
        exit()

answer = 0

for i in range(len(coin_list)-1, -1, -1):
    coin = coin_list[i]
    if K // coin > 0:
        answer += K // coin
        K -= coin * (K // coin)

    if K == 0:
        break

print(answer)

