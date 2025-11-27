from sys import stdin

n = int(stdin.readline().rstrip())
people = set()
gomgom = 0

for _ in range(n):
    log = stdin.readline().rstrip()
    if log == "ENTER":
        people = set()
    else: 
        if log not in people: gomgom += 1
        people.add(log)

print(gomgom)
