from sys import stdin, setrecursionlimit

def recursive(a, b, c):
	if b == 0: return 1
	x = recursive(a, b//2, c)
	val = (x * x) % c
	if b % 2 == 0: return val
	else: return (val * a) % c

a, b, c = map(int, stdin.readline().rstrip().split(" "))
print(recursive(a, b, c))