import sys

N = int(input())
Nlist = sorted(list(map(int, input().split(' '))))

M = int(input())
Mlist = list(map(int, input().split(' ')))

dictionary = {}

for i in Nlist:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for i in Mlist:
    if i in dictionary:
        print(dictionary[i], end = ' ')
    else:
        print(0, end = ' ')