def dfs(node):
	global adj_list, visited, cnt

	# base case
	if visited[node]:
		return
	visited[node] = True

	cnt += 1

	# recursive case
	for adj_node in adj_list[node]:
		dfs(adj_node)


# input
N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

visited = [False] * (N + 1)

# solve
cnt = 0
dfs(1)

print(cnt - 1)
