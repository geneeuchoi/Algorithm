from sys import stdin, setrecursionlimit

def check(distance):
	count = 1
	prev = homes[0]

	for i in range(1, n):
		current = homes[i]
		if current - prev >= distance:
			count += 1
			prev = current
	return count >= c


n, c = map(int, stdin.readline().rstrip().split(" "))
homes = []
for _ in range(n):
	tmp = int(stdin.readline().rstrip())
	homes.append(tmp)
homes.sort()

low, high, answer = 1, homes[n-1], 0
while low <= high:
	mid = (low + high) // 2
	if check(mid):
		answer = mid
		low = mid+1
	else:
		high = mid-1
print(answer)