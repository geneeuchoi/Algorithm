from collections import deque
import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10000000)

# 상하좌우 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N) and (0<=ny<M) and graph[nx][ny] == 0: #-1은 방문 x
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


# 가로 M 세로 N
# row N, i column M, j
M, N = map(int, input().split())

graph = [[0] * M for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

q = deque([]) # x, y 좌표

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])
bfs()

max = 0

for i in range(N):
    for j in range(M):
        if max < graph[i][j]:
            max = graph[i][j]

        if graph[i][j] == 0:
            print(-1)
            exit() # 종료

print(max-1)
