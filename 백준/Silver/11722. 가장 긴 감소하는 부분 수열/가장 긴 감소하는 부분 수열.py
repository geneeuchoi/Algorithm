from sys import stdin, setrecursionlimit

def find():
	dp = [1] * (n + 1)
	for i in range(1, n + 1):
		for j in range(1, i):
			if sequence[j] > sequence[i]: 
				dp[i] = max(dp[i], dp[j] + 1)

	return max(dp)


n = int(stdin.readline().rstrip())
sequence = [0] + list(map(int, stdin.readline().rstrip().split(" ")))
print(find())