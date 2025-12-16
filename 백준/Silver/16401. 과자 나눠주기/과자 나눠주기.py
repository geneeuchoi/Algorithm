from sys import stdin

m, n = map(int, stdin.readline().rstrip().split(" "))
snacks = list(map(int, stdin.readline().rstrip().split(" ")))
snacks.sort(reverse=True)

low, high = 1, snacks[0]
answer = 0
while low <= high:
	mid = (low+high)//2
	cnt = 0
	for snack in snacks:
		if snack < mid: break

		val = snack // mid
		cnt += val
		if cnt >= m: break
	
	if cnt >= m:
		answer = mid
		low = mid + 1
	else:
		high = mid - 1
print(answer)