from sys import stdin

# a, b, c, d, e, f = map(int, stdin.readline().rstrip().split(' '))

N = int(stdin.readline().rstrip())
a_list = []
for _ in range(N):
    a_list.append(int(stdin.readline().rstrip()))

a_list.sort()
for elem in a_list:
    print(elem)