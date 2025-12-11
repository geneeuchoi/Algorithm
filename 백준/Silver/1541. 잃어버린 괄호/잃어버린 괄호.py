from sys import stdin, setrecursionlimit


expressions = stdin.readline().rstrip()
group = expressions.split("-")

for i in range(len(group)):
	expression = group[i]
	if "+" in expression:
		group[i] = sum(map(int, expression.split("+")))
	if type(group[i]) != "str":
		group[i] = int(group[i])

answer = group[0]
for i in range(1, len(group)):
	answer -= group[i]
print(answer)

