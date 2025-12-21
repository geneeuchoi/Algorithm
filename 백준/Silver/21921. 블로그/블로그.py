from sys import stdin
import heapq

n, x = map(int, stdin.readline().rstrip().split(" "))
visitors = list(map(int, stdin.readline().rstrip().split(" ")))
dp = [visitors[0]]+[0 for _ in range(n-1)]
for i in range(1, n):
	dp[i] = dp[i-1]+visitors[i]

same = 0
max_visit = 0
for i in range(x-1, n):
	start = i-x
	visitors_num = dp[i]
	if start >= 0: visitors_num = dp[i]-dp[start]
	
	if visitors_num > max_visit: 
		max_visit = visitors_num
		same = 0
	if visitors_num == max_visit: 
		same += 1

if max_visit == 0: print("SAD")
else:
	print(max_visit)
	print(same)