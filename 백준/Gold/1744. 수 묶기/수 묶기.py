from sys import stdin

N = int(stdin.readline().strip())
positive_list, zero_list, negative_list = [], [], []

for _ in range(N):
    tmp = int(stdin.readline().strip())
    if tmp > 0: positive_list.append(tmp)
    elif tmp == 0: zero_list.append(tmp)
    else: negative_list.append(tmp)

positive_list.sort(reverse = True)
negative_list.sort()
answer = 0

if len(negative_list) % 2 == 0:
    for i in range(0, len(negative_list), 2):
        tmp_mul = negative_list[i] * negative_list[i+1]
        tmp_sum = negative_list[i] + negative_list[i+1]
        if tmp_mul > tmp_sum: answer += tmp_mul
        else: answer += tmp_sum
else:
    for i in range(0, len(negative_list)-1, 2):
        tmp_mul = negative_list[i] * negative_list[i+1]
        tmp_sum = negative_list[i] + negative_list[i+1]
        if tmp_mul > tmp_sum: answer += tmp_mul
        else: answer += tmp_sum
    if len(zero_list) == 0:
        answer += negative_list[len(negative_list)-1]

if len(positive_list) % 2 == 0:
    for i in range(0, len(positive_list), 2):
        tmp_mul = positive_list[i] * positive_list[i+1]
        tmp_sum = positive_list[i] + positive_list[i+1]
        if tmp_mul > tmp_sum: answer += tmp_mul
        else: answer += tmp_sum
else:
    for i in range(0, len(positive_list)-1, 2):
        tmp_mul = positive_list[i] * positive_list[i+1]
        tmp_sum = positive_list[i] + positive_list[i+1]
        if tmp_mul > tmp_sum: answer += tmp_mul
        else: answer += tmp_sum
    answer += positive_list[len(positive_list)-1]

print(answer)