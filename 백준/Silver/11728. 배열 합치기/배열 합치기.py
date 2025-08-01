from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A_end, B_end = N, M
A_start, B_start = 0, 0

result = []

while A_start < A_end and B_start < B_end:
    if A[A_start] == B[B_start]:
        result.append(str(A[A_start]))
        A_start += 1
    elif A[A_start] < B[B_start]:
        result.append(str(A[A_start]))
        A_start += 1
    else:
        result.append(str(B[B_start]))
        B_start += 1

while A_start < A_end:
    result.append(str(A[A_start]))
    A_start += 1

while B_start < B_end:
    result.append(str(B[B_start]))
    B_start += 1

stdout.write(' '.join(result))
