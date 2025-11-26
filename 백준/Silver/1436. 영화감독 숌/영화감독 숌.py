from sys import stdin

# a, b, c, d, e, f = map(int, stdin.readline().rstrip().split(' '))

N = int(stdin.readline().rstrip())
step = 0
for i in range(666, 200000001):
    if "666" in str(i): step += 1
    if step == N:
        print(i)
        break