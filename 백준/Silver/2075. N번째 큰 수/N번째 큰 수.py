from sys import stdin
import heapq

n = int(stdin.readline().rstrip())
heap = []
for _ in range(n):
	tmp = list(map(int, stdin.readline().rstrip().split(" ")))
	for item in tmp:
		if len(heap) < n:
			heapq.heappush(heap, item)
		else:
			if item > heap[0]:
				heapq.heappushpop(heap, item)

print(heap[0])