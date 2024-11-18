import sys

# 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, input().split(' '))

KList = []
for _ in range(K):
    KList.append(int(input()))

def bs(KList, N):
    left = 1
    right = max(KList)

    while(left <= right):
        maxNum = 0
        mid = (left + right) // 2

        for i in KList:
            maxNum += i // mid

        
        if maxNum >= N:
            left = mid + 1
        else:
            right = mid - 1
    return right
            

print(bs(KList, N))