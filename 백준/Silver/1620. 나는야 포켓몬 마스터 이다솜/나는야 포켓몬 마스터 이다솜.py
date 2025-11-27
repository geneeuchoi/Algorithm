from sys import stdin

n, m = map(int, stdin.readline().rstrip().split(" "))
pocketmon = dict()


for i in range(1, n+1):
    tmp = stdin.readline().rstrip()
    i_str = str(i)
    pocketmon[tmp] = i_str
    pocketmon[i_str] = tmp

for _ in range(m):
    tmp = stdin.readline().rstrip()
    print(pocketmon[tmp])