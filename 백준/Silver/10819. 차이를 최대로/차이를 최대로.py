from sys import stdin

def recursive(num_list, tmp_list, answer_list, visited):
	if 0 not in visited:
		answer = 0
		for i in range(len(tmp_list)-1):
			answer += abs(tmp_list[i] - tmp_list[i+1])
		answer_list.append(answer)
		return

	for i in range(len(num_list)):
		if visited[i] == 0: 
			visited[i] = 1
			tmp_list.append(num_list[i])
			recursive(num_list, tmp_list, answer_list, visited)
			visited[i] = 0
			tmp_list.pop()

T = int(stdin.readline().strip())
num_list = list(map(int, stdin.readline().strip().split(' ')))
tmp_list, answer_list = [], []
visited = [0] * T

recursive(num_list, tmp_list, answer_list, visited)

print(max(answer_list))