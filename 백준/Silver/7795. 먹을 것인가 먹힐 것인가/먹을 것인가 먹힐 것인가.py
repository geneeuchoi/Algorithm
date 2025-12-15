from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

t = int(stdin.readline().rstrip())
for _ in range(t):
	n, m = map(int, stdin.readline().rstrip().split(" "))
	a = list(map(int, stdin.readline().rstrip().split(" ")))
	b = list(map(int, stdin.readline().rstrip().split(" ")))
	b.sort()
	answer = 0

	for i in range(n):
		current = a[i]
		low, high = 0, m-1
		cnt = 0
		while(low <= high):
			mid = (low+high)//2
			if b[mid] < current: 
				cnt = mid + 1
				low = mid + 1
			elif b[mid] >= current: 
				high = mid -1
		answer += cnt
	print(answer)