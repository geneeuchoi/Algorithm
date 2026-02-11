from sys import stdin

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split(" ")))
a.sort()

left, right = 0, n-1
answer1, answer2 = 0, 0
min_sum = float('inf')

while left < right:
	current_sum = a[left] + a[right]

	if abs(current_sum) < min_sum: 
		min_sum = abs(current_sum)
		answer1, answer2 = a[left], a[right]

	if current_sum > 0: right -= 1
	elif current_sum < 0: left += 1
	else: 
		answer1, answer2 = a[left], a[right]
		break

print(answer1, answer2)