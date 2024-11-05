import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

# 상하좌우 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    visited[y][x] = 1
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0<= ny < N):
            if not visited[ny][nx] and graph[ny][nx]:
                count += dfs(ny, nx)
    return count

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 만큼 반복
for _ in range(T):
    # 가로 길이 M 세로 길이 N 배추 개수 K
    M, N, K = map(int, input().split())
    
    # 그래프, 방문 노드 초기화
    graph = [[0] * M for _ in range(N)] 
    visited = [[0] * M for _ in range(N)] 

    # 그래프에 배추 개수 초기화
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 컴포넌트 세기
    res = []
    for i in range(N): # 세로
        for j in range(M): # 가로
            if not visited[i][j] and graph[i][j]:
                res.append(dfs(i, j))

    print(len(res))

