from sys import stdin
import heapq

def check(x):
	if x == 0:
		if len(priority) == 0: 
			print(0)
		else: 
			min_val = heapq.heappop(priority)
			print(min_val)
	else: 
		heapq.heappush(priority, x)


n = int(stdin.readline().rstrip())
priority = []

for _ in range(n):
	x = int(stdin.readline().rstrip())
	check(x)
