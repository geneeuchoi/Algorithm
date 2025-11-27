from sys import stdin

n, m = map(int, stdin.readline().rstrip().split(" "))
frequent = dict()
for _ in range(n):
    word = stdin.readline().rstrip()
    if len(word) >= m:
        frequent[word] = frequent.get(word, 0) + 1

frequent_list = list(frequent.items())

frequent_list.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
words = list(elem[0] for elem in frequent_list)

for word in words:
    print(word)