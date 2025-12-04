from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def calculate(team):
	ability_sum = 0
	for i in team:
		for j in team:
			ability_sum += ability[i][j]
	return ability_sum

def devide(idx, start_t):
	if len(start_t) == n//2:
		link_t = all_members - start_t
		ability_diff.append(abs(calculate(start_t)-calculate(link_t)))
		return

	for i in range(idx, n):
		start_t.add(i)
		devide(i+1, start_t)
		start_t.remove(i)


n = int(stdin.readline().rstrip())
ability = []
for _ in range(n):
	ability.append(list(map(int, stdin.readline().rstrip().split(" "))))

all_members = set(range(n))
ability_diff = []
devide(0, set())
print(min(ability_diff))