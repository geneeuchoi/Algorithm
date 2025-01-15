N, M = map(int, input().split(' '))
MList = list(map(int, input().split(' ')))

baesuSet = set()

for num in MList:
	for i in range(1, 10000):
		if 1 <= num * i <= N:
			baesuSet.add(num * i)
		else:
			continue


print(sum(baesuSet))