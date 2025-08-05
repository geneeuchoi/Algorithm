from sys import stdin

E, S, M = map(int, stdin.readline().strip().split(' '))

for i in range(1, 200000000):
    e_val, s_val, m_val = 0, 0, 0

    if i % 15 == 0: e_val = 15
    else: e_val = i % 15

    if i % 28 == 0: s_val = 28
    else: s_val = i % 28

    if i % 19 == 0: m_val = 19
    else: m_val = i % 19

    if e_val == E and s_val == S and m_val == M:
        print(i)
        break