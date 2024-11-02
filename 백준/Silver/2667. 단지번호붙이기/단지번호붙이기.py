def dfs(x, y):
    global count
    count += 1
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * n for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            count = 0
            dfs(i, j)
            res.append(count)

print(len(res))
for i in sorted(res):
    print(i)