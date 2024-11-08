from collections import deque
import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10000000)

def bfs():
    q = deque()
    q.append(S-1)
    visited[S - 1] = 1 # 시작점 방문 처리

    while q:
        floor = q.popleft()
        # 이동한 층이 G와 일치할 시 
        if floor == G-1:
            print(visited[floor]-1) # 시작점 방문 처리해줬던 것 -1
            return
        # 그렇지 않을 경우
        for j in (floor+U, floor-D):
            if (0 <= j < F) and not visited[j]:
                visited[j] = visited[floor] + 1
                q.append(j)

    # 엘리베이터로 방문할 수 없는 경우
    if not visited[G-1]:
        print("use the stairs")


# 총 층수 F, 현재 층수 S, 스타트링크 층수 G, 위로 갈 수 있는 층수 U, 아래로 갈 수 있는 층수 D
F, S, G, U, D = map(int, input().split())

# 1층 이상 F층 이하
visited = [0] * F


bfs() 
