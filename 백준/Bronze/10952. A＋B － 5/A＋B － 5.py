import sys

sumValue = 1
while(sumValue != 0):
	A, B = map(int, sys.stdin.readline().split(' '))
	sumValue = A + B
	if(sumValue != 0):
		print(sumValue)