import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == False:
                if color == graph[nx][ny]:
                    dfs(nx, ny)
    

# ==============입력부===========

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]
# cnt1: 비색약인 구역 개수 cnt2: 색약인 구역 개수
cnt1, cnt2 = 0, 0


# ==============풀이==============
# 적록 색약 아닐 때
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            cnt1 += 1



# 적록 색약일 때
# G과 R 통일
for i in range(N):
	for j in range(N):
		if graph[i][j] == 'G':
			graph[i][j] = 'R'

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            cnt2 += 1


print(cnt1, cnt2)