from sys import stdin

n = int(stdin.readline().rstrip())
requests = list(map(int, stdin.readline().rstrip().split(" ")))
m = int(stdin.readline().rstrip())
max_req = max(requests)

if sum(requests) <= m: 
	print(max_req)
	exit()

low, high = 1, max_req
answer = 0
while low <= high:
	mid = (low+high)//2
	req_sum = 0
	for req in requests:
		val = 0
		if mid > req: val = req
		else: val = mid
		req_sum += val
	
	if req_sum > m:
		high = mid - 1
	elif req_sum == m:
		answer = mid
		break
	else:
		answer = mid
		low = mid + 1
print(answer)