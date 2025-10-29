import sys
from sys import stdin

# 입력1 
n1, n2, n3, n4, n5 = map(int, stdin.readline().strip().split(' '))
nSum = n1**2+n2**2+n3**2+n4**2+n5**2
print(nSum%10)