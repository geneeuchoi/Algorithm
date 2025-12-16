from sys import stdin

x, y = map(int, stdin.readline().rstrip().split(" "))
z = (y * 100) // x
low, high = 1, x
answer = -1

while low <= high:
	mid = (low+high)//2
	tmp_x, tmp_y = x+mid, y+mid
	tmp_z = int(tmp_y/tmp_x*100)
	if tmp_z > z:
		answer = mid
		high = mid-1
	elif tmp_z == z:
		low = mid+1


print(answer)