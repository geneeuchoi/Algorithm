from sys import stdin

n = int(stdin.readline().rstrip())
log = set()

for _ in range(n):
    tmp = stdin.readline().rstrip()
    name, state = tmp.split(" ")
    if state == "enter":
        log.add(name)
    else:
        log.remove(name)

log_list = list(log)
log_list.sort(key=lambda x: x, reverse = True)
for employee in log_list:
    print(employee)