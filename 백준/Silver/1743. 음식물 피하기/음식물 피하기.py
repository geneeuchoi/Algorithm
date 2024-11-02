import sys
sys.setrecursionlimit(10000)

def DFS(graph, visitied, x, y):
    global cnt
    visited[x][y] = cnt

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < N and 0 <= ny < M and not visitied[nx][ny] and graph[nx][ny]:
            cnt += 1
            DFS(graph, visited, nx, ny)
    

# ==============입력부===========
# N 세로 M 가로 K 음쓰 개수
N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 음쓰 위치 표기
for _ in range(K):
	Y, X = map(int, input().split())
	graph[Y-1][X-1] = 1

# ==============풀이==============
big = 0
for x in range(N):
    for y in range(M):
    	# 해당 좌표에 음쓰가 있고 방문하지 않은 경우
        if graph[x][y] and not visited[x][y]:
            cnt = 1
            DFS(graph, visited, x, y)
            big = max(cnt, big)
print(big)