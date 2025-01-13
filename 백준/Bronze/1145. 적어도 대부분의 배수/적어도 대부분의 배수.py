
# 배열 입력받기
seq = list(map(int, input().split(' ')))
seq.sort()

def findAnswer(seq):
	for i in range(seq[2], 1000000):
		cnt = 0
		for seqElem in seq:
			if i % seqElem == 0:
				cnt += 1
				if cnt == 3:
					return i

print(findAnswer(seq))