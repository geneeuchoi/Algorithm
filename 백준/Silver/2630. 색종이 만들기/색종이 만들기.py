from sys import stdin, setrecursionlimit

def check(size, x, y):
	first = paper[x][y]
	for i in range(x, x + size):
		for j in range(y, y + size):
			if paper[i][j] != first: return False
	return True

def recursive(n, x, y):
	global blue, white
	if check(n, x, y):
		first = paper[x][y]
		if first: blue += 1
		else: white += 1
		return
	else:
		size = n//2
		recursive(size, x, y)
		recursive(size, x, y+size)
		recursive(size, x+size, y)
		recursive(size, x+size, y+size)

n = int(stdin.readline().rstrip())
paper = []
for _ in range(n):
	paper.append(list(map(int, stdin.readline().rstrip().split(" "))))

blue, white = 0, 0
recursive(n, 0, 0)

print(white)
print(blue)