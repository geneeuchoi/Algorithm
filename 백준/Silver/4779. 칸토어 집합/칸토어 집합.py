from sys import stdin

def cantor(cantor_list, first_idx, last_idx):
	idx = (last_idx - first_idx)//3
	start = first_idx + idx
	end = start + idx

	if idx == 0: return 

	for i in range(start, end):
		cantor_list[i] = " "

	cantor(cantor_list, first_idx, start)
	cantor(cantor_list, end, last_idx)


try:
	while(True):
		n = int(stdin.readline().rstrip())
		cantor_list = ["-" for i in range (3**n)]
		cantor(cantor_list, 0, 3**n)
		for elem in cantor_list:
			print(elem, end = "")
		print()
except:
	exit(0)