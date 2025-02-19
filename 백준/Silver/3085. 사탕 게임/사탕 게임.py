#N, M = map(int, sys.stdin.readline().rstrip().split(' '))
import sys
import copy

def findMaxCnt(N, rectangle):
    maxCntList = []
    # 행
    for i in range(N):
        maxCnt = 1  
        for j in range(1, N):
            if rectangle[i][j] == rectangle[i][j - 1]:
                maxCnt += 1
            else:
                maxCntList.append(maxCnt)
                maxCnt = 1 
        maxCntList.append(maxCnt)

  # 열 검사
    for j in range(N):
        maxCnt = 1
        for i in range(1, N):
            if rectangle[i][j] == rectangle[i - 1][j]:
                maxCnt += 1
            else:
                maxCntList.append(maxCnt)
                maxCnt = 1
        maxCntList.append(maxCnt) 

    return max(maxCntList)

def switch(N, rectangle, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    maxCandy = 0 

    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < N and 0 <= nj < N: 
            rectangle[i][j], rectangle[ni][nj] = rectangle[ni][nj], rectangle[i][j]
            maxCandy = max(maxCandy, findMaxCnt(N, rectangle))
            rectangle[i][j], rectangle[ni][nj] = rectangle[ni][nj], rectangle[i][j]  # 원상복구

    return maxCandy

N = int(sys.stdin.readline().rstrip())
rectangle = []
for i in range(N):
    rectangle.append(list(sys.stdin.readline().rstrip()))

maxCandy = 0

for i in range(N):
    for j in range(N):
        maxCandy = max(maxCandy, switch(N, rectangle, i, j))

print(maxCandy)