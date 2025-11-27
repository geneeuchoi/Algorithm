from sys import stdin

a_len, b_len = map(int, stdin.readline().rstrip().split(" "))
a = set(map(int, stdin.readline().rstrip().split(" ")))
b = set(map(int, stdin.readline().rstrip().split(" ")))

a_first = a - b
b_first = b - a
symmetry = a_first.union(b_first)
print(len(symmetry))