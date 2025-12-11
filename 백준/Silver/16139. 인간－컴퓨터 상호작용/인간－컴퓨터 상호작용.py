from sys import stdin, setrecursionlimit

# s 문자열
# q 질문 개수
s = stdin.readline().rstrip()
q = int(stdin.readline().rstrip())
len_s = len(s)

dp = [[0] * (len_s+1) for _ in range(26)]
for i in range(len_s):
    current_idx = ord(s[i]) - ord('a')
    for j in range(26):
        dp[j][i + 1] = dp[j][i]
    dp[current_idx][i+1] += 1

for i in range(q):
	a, l, r = stdin.readline().rstrip().split(" ")
	l, r = int(l), int(r)

	a_idx = ord(a) - ord('a')
	result = dp[a_idx][r+1] - dp[a_idx][l]
	print(result)