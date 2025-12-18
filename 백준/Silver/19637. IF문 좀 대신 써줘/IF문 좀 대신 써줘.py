from sys import stdin

def check(character):
	low_idx, high_idx = 0, n-1
	while low_idx <= high_idx:
		mid_idx = (low_idx+high_idx)//2
		mid = powers[mid_idx]
		if powers[mid_idx-1] < character and character <= mid:
			return ranks[mid_idx]
		if character <= mid:
			high_idx = mid_idx -1
		elif character > mid:
			low_idx = mid_idx + 1
	return ranks[mid_idx]

n, m = map(int, stdin.readline().rstrip().split(" "))
ranks, powers = [], []

for _ in range(n):
	rank, power = stdin.readline().rstrip().split(" ")
	ranks.append(rank)
	powers.append(int(power))

for _ in range(m):
	character = int(stdin.readline().rstrip())

	print(check(character))
