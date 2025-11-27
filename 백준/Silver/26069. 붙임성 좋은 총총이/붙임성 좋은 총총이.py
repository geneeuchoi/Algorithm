from sys import stdin

n = int(stdin.readline().rstrip())
dance = set()
dance.add("ChongChong")

for _ in range(n):
    a, b = map(str, stdin.readline().rstrip().split(" "))
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
