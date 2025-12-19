from sys import stdin
import heapq

def check(x):
	if x == 0:
		if not priority: print(0)
		else: print(heapq.heappop(priority)[1]) 
	else: 
		heapq.heappush(priority, (abs(x), x))

n = int(stdin.readline().rstrip())
priority = []

for _ in range(n):
	x = int(stdin.readline().rstrip())
	check(x)
