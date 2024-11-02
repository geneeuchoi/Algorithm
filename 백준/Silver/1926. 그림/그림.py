import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(y, x):
    visited[y][x] = 1
    count = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] and not visited[ny][nx]:
            count += dfs(ny, nx)
    return count

# 세로 n, 가로 m
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]
res = []

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            res.append(dfs(i, j))

print(len(res))
if len(res) == 0:
    print(0)
else:
    print(max(res))