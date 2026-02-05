from collections import deque

def solution(maps):
    # 가로, 세로
    n, m = len(maps), len(maps[0])
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 최단거리이므로 bfs -> queue
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx, my = x+dx[i], y+dy[i]
            
            if 0 <= mx < n and 0 <= my < m and maps[mx][my] == 1:
                maps[mx][my]=maps[x][y]+1
                queue.append((mx, my))

    answer = maps[n-1][m-1]
    return answer if answer > 1 else -1