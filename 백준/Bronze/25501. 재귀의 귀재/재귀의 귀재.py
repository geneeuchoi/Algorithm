from sys import stdin

def recursion(s, start, end, step):
	step += 1
	if start >= end: return (1, step)
	elif s[start] != s[end]: return (0, step)
	return recursion(s, start+1, end-1, step)

def isPalindrome(s):
	return recursion(s, 0, len(s)-1, 0)


t = int(stdin.readline().rstrip())
for _ in range(t):
	s = stdin.readline().rstrip()
	tmp = isPalindrome(s)
	print(tmp[0], tmp[1])
