from collections import deque
import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10000000)

def bfs():
    q = deque()

    q.append(N)
    visited[N] = 1

    while q:
        point = q.popleft()

        if point == K:
            print(sec[point])
            return
        
        for j in (point*2, point-1, point+1):
            if (0 <= j <= 100000) and not visited[j]:
                visited[j] = 1

                if j == point*2:
                    sec[j] = sec[point]
                else:
                    sec[j] = sec[point]+1

                q.append(j)



# 수빈 N, 동생 K
N, K = map(int, input().split())

# 최대 100,000 까지 움직일 수 있다.
visited = [0] * 100001
sec = [0] * 100001

bfs() 
