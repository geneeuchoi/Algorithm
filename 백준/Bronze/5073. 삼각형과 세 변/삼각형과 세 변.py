from sys import stdin

def isTriangle(len1, len2, len3):
	tmp_list = [len1, len2, len3]
	max_len = max(tmp_list)
	sum_len = sum(tmp_list)

	if max_len >= sum_len - max_len:
		return False
	return True

len1, len2, len3 = map(int, stdin.readline().strip().split(' '))

while(len1 != 0 and len2 != 0 and len3 != 0):
	if not isTriangle(len1, len2, len3):
		print("Invalid")
	else:
		if len1==len2 and len2==len3 and len1==len3:
			print("Equilateral")
		elif len1 != len2 and  len1 != len3 and len3 != len2:
			print("Scalene")
		elif len1==len2 or len1==len3 or len2==len3:
			print("Isosceles")
	len1, len2, len3 = map(int, stdin.readline().strip().split(' '))