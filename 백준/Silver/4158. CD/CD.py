from sys import stdin


n, m = map(int, stdin.readline().rstrip().split(" "))

while n != 0 and m != 0:
	cds = dict()
	for _ in range(n+m):
		val = int(stdin.readline().rstrip())
		cds[val] = cds.get(val, 0) + 1
	vals = list(cds.values())
	cnt = 0
	for val in vals:
		if val >= 2: cnt += 1
	print(cnt)

	# for sang_cd in sanguen:
	# 	low, high = 0, m-1
	# 	while low <= high:
	# 		mid = (low+high)//2
	# 		sun_cd = sunyoung[mid]
	# 		if sun_cd == sang_cd: 
	# 			cnt += 1
	# 			break
	# 		elif sun_cd < sang_cd:
	# 			low = mid + 1
	# 		elif sun_cd > sang_cd:
	# 			high = mid -1
	# print(cnt)
	n, m = map(int, stdin.readline().rstrip().split(" "))