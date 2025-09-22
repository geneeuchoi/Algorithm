from sys import stdin

H, W = map(int, stdin.readline().split())
blocks = list(map(int, stdin.readline().split()))

left, right = 0, W - 1
left_max, right_max = 0, 0
rain = 0

while left < right:
    if blocks[left] <= blocks[right]:
        if blocks[left] >= left_max:
            left_max = blocks[left]
        else:
            rain += left_max - blocks[left]
        left += 1
    else:
        if blocks[right] >= right_max:
            right_max = blocks[right]
        else:
            rain += right_max - blocks[right]
        right -= 1

print(rain)
