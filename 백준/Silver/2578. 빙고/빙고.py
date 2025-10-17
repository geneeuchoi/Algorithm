import sys
from sys import stdin

def say(cs, ms_val, bg_table):
    for i in range(5):
        for j in range(5):
            if cs[i][j] == ms_val:
                bg_table[i][j] = 1
                return

def check(bg_table, bg_cnt):
    bg_cnt += line(bg_table)
    bg_cnt += diagonal(bg_table)

    if bg_cnt >= 3: return True
    else: return False

def line(bg_table):
    rise = 0
    for i in range(5):
        flag1, flag2 = True, True
        for j in range(5):
            # 가로
            if bg_table[i][j] != 1: flag1 = False
            # 세로
            if bg_table[j][i] != 1: flag2 = False

        if flag1 == True: rise += 1
        if flag2 == True: rise += 1

    return rise


def diagonal(bg_table):
    flag1 = flag2 = True
    rise = 0

    for i in range(5):
        # 1. 왼쪽-오른쪽
        if bg_table[i][i] != 1:
            flag1 = False

        # 2. 오른쪽-왼쪽
        if bg_table[i][4-i] != 1:
            flag2 = False

    if flag1 == True: rise += 1
    if flag2 == True: rise += 1

    return rise

# 입력
cs = []
for _ in range(5):
    cs.append(list(map(int, stdin.readline().strip().split(' '))))

ms = []
for _ in range(5):
    ms.append(list(map(int, stdin.readline().strip().split(' '))))

bg_table = [[0] * 5 for _ in range(5)]
bg_cnt = step = 0


# 사회자가 부르는 값
for i in range(5):
    for j in range(5):
        step += 1
        say(cs, ms[i][j], bg_table)

        if check(bg_table, bg_cnt):
            print(step)
            exit(0)

