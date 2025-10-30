import sys
from sys import stdin

while(True):
    try:
        triangle = list(map(int, stdin.readline().strip().split(" ")))
        if 0 in triangle: exit(0)
        
        triangle.sort()
        if (triangle[0]**2 + triangle[1]**2 == triangle[2]**2): 
            print("right")
        else: 
            print("wrong")
    except:
        exit(0)