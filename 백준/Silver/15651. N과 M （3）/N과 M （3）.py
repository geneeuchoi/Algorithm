from sys import stdin

def recursive(end, step, tmp):
	if step == m: 
		available.append(tmp)
		return

	for i in range(1, end):
		recursive(end, step+1, tmp + [i])

n, m = map(int, stdin.readline().rstrip().split(" "))
available = []
recursive(n+1, 0, [])

for available_elem in available:
	for elem in available_elem:
		print(elem, end = " ")
	print()