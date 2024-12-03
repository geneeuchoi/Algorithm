r, c = map(int, input().split(' '))
seq = []

for _ in range(r):
    seq.append(list(input().strip()))

dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]

max_count = 0

def dfs(x, y, visited, cnt):
    global max_count
    max_count = max(max_count, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r and seq[ny][nx] not in visited:
            visited.add(seq[ny][nx])  # 현재 문자 추가
            dfs(nx, ny, visited, cnt + 1)
            visited.remove(seq[ny][nx])  # 탐색 종료 후 복원

visited = set()
visited.add(seq[0][0])
dfs(0, 0, visited, 1)

print(max_count)