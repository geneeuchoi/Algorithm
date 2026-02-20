def dfs(node, graph, visited):
    visited[node] = 1
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, graph, visited)
    return count

def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if j == i: continue
            v1, v2 = wires[j][0], wires[j][1]
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [0 for _ in range(n+1)]
        count = dfs(1, graph, visited)
        answer.append(abs(count - (n-count)))
        
    return min(answer)