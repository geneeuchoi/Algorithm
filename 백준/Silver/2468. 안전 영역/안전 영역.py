import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

# 상하좌우 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x, h):
    count =  1
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0<= ny < N):
            if not visited[ny][nx] and graph[ny][nx] > h:
                dfs(ny, nx, h)
    return count

# 행, 열
N = int(input())

# 그래프, 방문 노드 초기화
graph = [[] for _ in range(N)] 

# 그래프 높이 최소화
for i in range(N):
    graph[i] = list(map(int, input().split(' ')))

# 안전높이가 그래프의 최댓값 이상이 되면 모두 물에 잠기므로 그 이상의 값은 모두 물에 잠기게 된다.
# 안전높이 이상의 값을 반복할 필요가 없으므로 그래프의 최댓값을 구해준다.
maxHeight = max(map(max, graph))
answer = []

for h in range(0, maxHeight+1):
    visited = [[0] * N for _ in range(N)] 
    res = []
    for x in range(N):
        for y in range(N):
            if not visited[y][x] and graph[y][x] > h:
                res.append(dfs(y, x, h))
                answer.append(len(res))

print(max(answer))
