from sys import stdin

n = int(stdin.readline().rstrip())
for i in range(n):
	for j in range(n-i-1):
		print(" ", end="")
	for k in range(i*2+1):
		print("*", end="")
	print()
for i in range(1, n):
	for k in range(i):
		print(" ", end="")
	for j in range((n-i-1)*2+1):
		print("*", end="")
	print()