X = int(input())
N = int(input())

sumPrice = 0
for i in range(N):
	A, B = map(int, input().split(' '))
	sumPrice += A * B

if sumPrice == X:
	print("Yes")
else:
	print("No")