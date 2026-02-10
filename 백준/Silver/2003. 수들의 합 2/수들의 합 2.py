from sys import stdin

n, m = map(int, stdin.readline().rstrip().split(" "))
a = list(map(int, stdin.readline().rstrip().split(" ")))

left = 0
current_sum = 0
answer = 0

for right in range(n):
	current_sum += a[right]

	while current_sum > m:
		current_sum -= a[left]
		left += 1

	if current_sum == m: 
		answer += 1


print(answer)