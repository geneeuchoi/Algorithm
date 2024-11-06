from collections import deque
import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10000000)

def bfs():
    q = deque()
    q.append(N)
    while q:
        node = q.popleft()
        if node == K:
            print(visited[node])
            break
        for j in (node-1, node+1, node*2):
            if (0<=j<=MAX) and not visited[j]:
                visited[j] = visited[node] + 1
                q.append(j)

# 수빈 N 동생 K
N, K = map(int, input().split())

# 움직일 수 있는 최대 노드
MAX = 100000

# 0 이상 10,0000 이하. 방문했다는 것을 알려줌과 동시에 최단 시간을 알려준다.
visited = [0] * (MAX + 1)

bfs() 
