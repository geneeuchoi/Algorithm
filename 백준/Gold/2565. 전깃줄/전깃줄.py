from sys import stdin, setrecursionlimit

n = int(stdin.readline().rstrip())
dp, wires = [1 for _ in range(n)], []

for _ in range(n):
	wires.append(list(map(int, stdin.readline().rstrip().split(" "))))

wires.sort(key=lambda x: x[0])

# 현재 줄: i
for i in range(1, n):
	# 그 전의 줄 확인: j
	for j in range(i):
		# 현재 줄이 그 전 줄보다 크다면 꼬이지 않음
		if wires[i][1] > wires[j][1]:
			dp[i] = max(dp[i], dp[j]+1)

# dp 결과 = 최장 수열. 최고로 길게 만들 수 있는 경우
print(n - max(dp))
