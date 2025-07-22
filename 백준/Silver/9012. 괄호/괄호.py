import sys

def isVPS(ps, right):
    for i in range(len(ps)-1, -1, -1):
        if ps[i] == ')': right += 1
        else: right -= 1

        if right < 0:
            return print('NO')

    if right == 0:
        print('YES')
    else:
        print('NO')


N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    ps = sys.stdin.readline().strip()
    right = 0
    isVPS(ps, right)