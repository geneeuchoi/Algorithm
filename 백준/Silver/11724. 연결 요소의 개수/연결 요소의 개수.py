import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(y):
    visited[y] = 1
    count = 1
    for i in graph[y]:
        if not visited[i]:
            count += dfs(i)
    return count

# 정점 n, 간선 m
n, m = map(int, input().split())
graph = [[] for _ in range(n)] 
for _ in range(m):
    i, elem = map(int, input().split())
    graph[i-1].append(elem-1)
    graph[elem-1].append(i-1)
visited = [0] * n

res = []

for i in range(n):
    if not visited[i]:
        res.append(dfs(i))

print(len(res))