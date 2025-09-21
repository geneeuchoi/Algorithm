from sys import stdin

P = int(stdin.readline().strip())

for _ in range(P):
	students = list(map(int, stdin.readline().strip().split()))
	tmp = []
	step_sum = 0

	tmp.append(students[1])
	for i in range(2, 21):
		student = students[i]
		placed = 1
		for j in range(len(tmp)):
			if tmp[j] > student:
				step_sum += len(tmp) - j
				tmp.insert(j, student)
				placed = 0
				break
		if placed:
			tmp.append(student)
			
	print(students[0], step_sum)

