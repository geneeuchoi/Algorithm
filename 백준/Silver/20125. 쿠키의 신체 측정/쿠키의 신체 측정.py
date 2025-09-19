from sys import stdin

N = int(stdin.readline().strip())
cookie = []

for i in range(N):
	cookie.append(list(stdin.readline().strip()))

head_x, head_y, heart_x, heart_y = 0, 0, 0, 0

for i in range(N):
	for j in range(N):
		if cookie[i][j] == '*':
			head_x, head_y = i, j
			heart_x, heart_y = head_x + 1, head_y
	if head_x != 0 or head_y != 0:
		break

back_x, back_y = 0, heart_y

for i in range(head_x + 2, N):
	if cookie[i][heart_y] != "*":
		back_x = i - 1
		break

left_arm_x, left_arm_y = heart_x, 0
right_arm_x, right_arm_y = heart_x, 0

for i in range(0, heart_y):
	if cookie[heart_x][i] == "*":
		left_arm_y = i
		break

for i in range(N-1, heart_y, -1):
	if cookie[heart_x][i] == "*":
		right_arm_y = i
		break


left_leg_x, left_leg_y = 0, back_y-1
right_leg_x, right_leg_y = 0, back_y+1

for i in range(back_x+1, N):
	if cookie[i][left_leg_y] == "*":
		left_leg_x = i
	if cookie[i][right_leg_y] == "*":
		right_leg_x = i

print(heart_x+1, heart_y+1)
print(heart_y-left_arm_y, right_arm_y-heart_y, back_x - heart_x, left_leg_x-back_x, right_leg_x-back_x)


# print(심장x, 심장y)
# print(왼팔 길이, 오른팔, 왼다리, 오른다리)