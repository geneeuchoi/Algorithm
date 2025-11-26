from sys import stdin

# a, b, c, d, e, f = map(int, stdin.readline().rstrip().split(' '))

a_list = []
for _ in range(5):
    a_list.append(int(stdin.readline().rstrip()))

a_list.sort()
print(sum(a_list) // 5)
print(a_list[2])