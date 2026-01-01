from sys import stdin

S = set()

def add(x):
	S.add(x)

def remove(x):
	S.discard(x)

def check(x):
	flag = x in S
	print(int(flag))

def toggle(x):
	if x in S: S.remove(x)
	else: S.add(x)

def all():
	global S
	S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

def empty():
	S.clear()

M = int(stdin.readline().rstrip())
for _ in range(M):
	input_str = list(stdin.readline().rstrip().split(" "))
	op, x= input_str[0], 0
	if len(input_str) == 2: x = int(input_str[1])

	if op == "add": add(x)
	elif op == "check": check(x)
	elif op == "remove": remove(x)
	elif op == "toggle": toggle(x)
	elif op == "all": all()
	else: empty()

