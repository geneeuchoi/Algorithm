from sys import stdin

N = int(stdin.readline())
meetings = list(map(int, stdin.readline().split(' ')))
meetings.sort()

tmp, answer = 0, 0
for i in meetings:
    tmp += i
    answer += tmp

print(answer)