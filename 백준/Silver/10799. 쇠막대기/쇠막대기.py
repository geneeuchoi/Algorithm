import sys

place = sys.stdin.readline().strip()
pipe, pieces = 0, 0

for i in range(len(place)):
    if place[i] == '(':
        pipe += 1
    else:
        pipe -= 1
        if place[i-1] == '(':
            pieces += pipe
        else:
            pieces += 1

print(pieces)

