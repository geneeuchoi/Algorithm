from sys import stdin

T = int(stdin.readline().rstrip())
case = 0
for _ in range(T):
    N, M = map(int, stdin.readline().rstrip().split(" "))
    sum_1, sum_2 = 1, 1

    for i in range(M-N+1, M+1):
        sum_1 *= i
        
    for i in range(1, N+1):
        sum_2 *= i

    print(sum_1 // sum_2)
