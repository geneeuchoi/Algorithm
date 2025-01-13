
# 배열 입력받기
seq = [[] for _ in range(9)]

for i in range(9):
	seq[i]= list(map(int, input().split(' ')))


maxValue = 0
maxRow = 0
maxColumn = 0
for i in range(9):
	for j in range(9):
		if seq[i][j] >= maxValue:
			maxRow, maxColumn = i, j
			maxValue = seq[i][j]

print(maxValue)
print(maxRow+1, maxColumn+1)
