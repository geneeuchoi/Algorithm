from sys import stdin

N = int(stdin.readline().rstrip())


for i in range(N//5, -1, -1):
    n3 = (N - i * 5)//3
    envelop = i + n3

    if i * 5 + n3 *3 != N: continue
    else: 
        print(envelop)
        exit()

print(-1)