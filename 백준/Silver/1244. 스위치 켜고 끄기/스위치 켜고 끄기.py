import sys
from sys import stdin

def male(num, switche_state):
    for i in range(num-1, len(switche_state), num):
        switche_state[i] = int(not switche_state[i])

def female(num, switche_state):
    # 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 
    # 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
    # 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
    n = len(switche_state)
    L = R = num
    while L - 1 >= 0 and R + 1 < n and switche_state[L - 1] == switche_state[R + 1]:
        L -= 1
        R += 1
    
    for j in range(L, R+1):
        switche_state[j] = int(not switche_state[j])

# 입력
switche = int(stdin.readline().strip())
switche_state = list(map(int, stdin.readline().strip().split(' ')))
student = int(stdin.readline().strip())

# 처리
for _ in range(student):
    sex, num = map(int, stdin.readline().strip().split(' '))
    if sex == 1: male(num, switche_state)
    else: female(num-1, switche_state)

# 출력
for i in range(0, switche, 20):
    print(" ".join(map(str, switche_state[i:i+20])))