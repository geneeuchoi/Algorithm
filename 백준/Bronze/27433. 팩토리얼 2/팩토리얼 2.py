from sys import stdin

def factorial(n):
	if n == 0: return 1
	return n * factorial(n-1)


n = int(stdin.readline().rstrip())
print(factorial(n))