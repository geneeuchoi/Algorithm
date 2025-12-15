from sys import stdin

def check(mid):
	previous = 0
	for light in x:
		start = light - mid
		if previous < start: return False
		end = light + mid
		previous = end
	if end < n: return False
	return True

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
x = list(map(int, stdin.readline().rstrip().split(" ")))

height = 1
low, high = 1, n

while(low <= high):
	mid = (low+high)//2
	if check(mid):
		height = mid
		high = mid -1
	else:
		low = mid + 1
print(height)