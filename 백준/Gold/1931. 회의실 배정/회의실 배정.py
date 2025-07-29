from sys import stdin

N = int(stdin.readline())
meetings = [list(map(int, stdin.readline().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
last_end, cnt = meetings[0][1], 1

for i in range(1, len(meetings)):
    start = meetings[i][0]
    if last_end <= start:
        cnt += 1
        last_end = meetings[i][1]

print(cnt)