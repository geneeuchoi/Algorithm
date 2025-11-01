import sys
from sys import stdin

L = int(stdin.readline().rstrip())
string = stdin.readline().rstrip()

M, r = 1234567891, 31
hash_result, power = 0, 1
for ch in string:
    value = ord(ch) - 96
    hash_result = (hash_result + value * power) % M
    power = (power * r) % M

print(hash_result)