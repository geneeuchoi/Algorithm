import sys
from sys import stdin

while True:
    M, N = map(int, stdin.readline().rstrip().split(" "))
    if M == 0 and N == 0: exit()
    print(M+N)