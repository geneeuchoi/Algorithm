import sys
from sys import stdin

L = int(stdin.readline().strip())
string = stdin.readline().strip()
hash_result = 0
for i in range(L):
    hash_result += (ord(string[i:i+1])-96) * (31 ** i)

print(hash_result)