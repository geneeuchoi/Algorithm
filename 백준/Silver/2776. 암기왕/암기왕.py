from sys import stdin

t = int(stdin.readline().rstrip())
for _ in range(t):
	n = int(stdin.readline().rstrip())
	n_arr = list(map(int, stdin.readline().rstrip().split(" ")))
	n_arr.sort()

	m = int(stdin.readline().rstrip())
	m_arr = list(map(int, stdin.readline().rstrip().split(" ")))
	
	for i in range(m):
		m_current = m_arr[i]
		low, high = 0, n-1
		answer = 0

		while(low <= high):
			mid = (low+high)//2
			n_current = n_arr[mid]
			if n_current == m_current:
				answer = 1
				break
			elif n_current < m_current:
				low = mid + 1
			elif n_current > m_current: 
				high = mid -1
		print(answer)