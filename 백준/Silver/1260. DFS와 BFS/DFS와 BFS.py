# 정점의 개수 n, 간선의 개수 m, 탐색시작 정점의 번호 v
# 간선 양방향
# 첫째 줄에 dfs 수행결과
# 둘째 줄에 bfs 수행결과

from collections import deque

# 깊이 우선
def solve_dfs(node):
	global adj_list, visited
	
	# 노드에 방문한 적이 있다면 방문하지 않는다.
	if visited[node]:
		return
	
	# 방문한 적이 없다면 방문하고, 방문했다고 바꿔준다.
	visited[node] = True

	print(node, end=' ')

	# 노드를 하나씩 방문해준다. (재귀)
	for adj_node in adj_list[node]:
		solve_dfs(adj_node)


# 너비 우선
def solve_bfs(snode):
	global adj_list, visited

	# 처음 시작하는 노드를 큐에 넣어주고, 노드를 방문했다고 표시
	q = deque()
	q.append(snode)
	visited[snode] = True

	# 이후 남은 노드 방문
	while q:
		node = q.popleft()
		print(node, end=' ')

		for adj_node in adj_list[node]:
			if visited[adj_node]:
				continue
			q.append(adj_node)
			visited[adj_node] = True


# ==========입력 처리하기===========

# 공백을 기준으로 나눈 리스트 반환 ["N", "M", "V"]
# 문자열을 int 타입으로 변환한 리스트로 변환[N, M, V]
N, M, V = map(int, input().split())

# 정점의 개수 만큼 인접 리스트 생성
adj_list = [[] for _ in range(N + 1)]

# 간선의 개수만큼 반복
# input으로 받은 노드간의 연결을 인접 리스트에 넣어준다.
for _ in range(M):
	a, b = map(int, input().split())
	# a번째 리스트에 b를 넣음 -> a와 b가 연결됨
	adj_list[a].append(b)
	# 양방향 관계이므로 b도 a와 연결되어야 한다
	# b번째 리스트에 a를 넣음 -> b와 a가 연결됨
	adj_list[b].append(a)

# 노드 번호가 작은 것을 먼저 방문한다.
for node in range(1, N + 1):
	adj_list[node].sort()




# ==========문제 풀이===========
# 각 정점에 방문했는지 나타내는 리스트 생성
visited = [False] * (N + 1)
solve_dfs(V) # V: 시작 노드 번호
print()

visited = [False] * (N + 1)
solve_bfs(V)
print()
