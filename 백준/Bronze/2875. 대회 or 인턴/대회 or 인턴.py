import sys

N, M, K = map(int, sys.stdin.readline().strip().split(' '))

# K의 값을 적절하게 나누는 경우도 생각해야 한다.
# K를 나눌 수 있는 모든 경우를 찾는다.
K_list, answer_list = [], []
for i in range(K+1):
    K_list.append((K - i, i))

for K_list_elem in K_list:
    N_intern, M_intern = (N - K_list_elem[0]) // 2, M - K_list_elem[1]
    if N_intern > 0 and M_intern > 0:
        if N_intern <= M_intern: answer_list.append(N_intern)
        else: team = answer_list.append(M_intern)
    else:
        answer_list.append(0)

print(max(answer_list))