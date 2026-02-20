from collections import deque

def bfs(start, end, maps):
    n, m = len(maps), len(maps[0])
    start_x, start_y = start
    end_x, end_y = end
    
    queue = deque([(start_x, start_y, 0)])
    
    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1    
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while queue:
        curr_x, curr_y, dist = queue.popleft()
        if curr_x == end_x and curr_y == end_y: return dist
        
        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return -1
    
    

def solution(maps):
    s1, s2, e1, e2, l1, l2 = 0, 0, 0, 0, 0, 0
    
    for row in range(len(maps)):
        for column in range(len(maps[row])):
            if maps[row][column] == "S":
                s1, s2 = row, column
            elif maps[row][column] == "E":
                e1, e2 = row, column
            elif maps[row][column] == "L":
                l1, l2 = row, column
    
    s_e, e_l = bfs([s1, s2], [l1, l2], maps), bfs([l1, l2], [e1, e2], maps)
    if s_e == -1 or e_l == -1: return -1
    
    return s_e + e_l