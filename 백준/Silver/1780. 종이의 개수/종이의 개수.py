from sys import stdin

def devide_paper(length, i_start, j_start):
    global negative, zero, positive
    # 길이 확인하고 0이면 변수 개수 늘리고 리턴
    if length == 1:
        val = procession[i_start][j_start]
        if val == 0: zero += 1
        elif val > 0: positive += 1
        else: negative += 1
        return

    # 모두 같은 수로 되어있는지 확인한다.
    # 같은 수로 되어있으면 각각의 변수 개수 늘리고 리턴
    val = procession[i_start][j_start]
    is_same = True
    for i in range(i_start, i_start + length):
        for j in range(j_start, j_start + length):
            if procession[i][j] != val:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        if val == 0: zero += 1
        elif val > 0: positive += 1
        else: negative += 1
        return

    new_length = length // 3
    for i in range(3): 
        for j in range(3): 
            new_i = i_start + i * new_length
            new_j = j_start + j * new_length
            devide_paper(new_length, new_i, new_j)


N = int(stdin.readline().strip())
procession = []

for _ in range(N):
    procession.append(list(map(int, stdin.readline().strip().split(' '))))

negative, zero, positive = 0, 0, 0

devide_paper(N, 0, 0)

print(negative)
print(zero)
print(positive)
