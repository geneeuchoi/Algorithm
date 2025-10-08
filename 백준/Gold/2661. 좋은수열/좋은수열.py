import sys
from sys import stdin

def bt(N, answer):
    if len(answer) == N:
        print(answer)
        sys.exit(0)

    for ch in '123': 
        tmp = answer + ch
        lt = len(tmp)

        ok = True
        for j in range(1, lt // 2 + 1):
            if tmp[-j:] == tmp[-2*j:-j]:
                ok = False
                break

        if ok:
            bt(N, tmp)

N = int(stdin.readline().strip())
bt(N, "")