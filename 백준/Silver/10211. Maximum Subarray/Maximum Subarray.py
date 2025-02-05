import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    maxAnswers = -1000
    for i in range(0, N):
        maxSub = list(X)
        for j in range(i, N-1):
            maxSub[j+1] += maxSub[j]
        if maxAnswers < max(maxSub): 
            maxAnswers = max(maxSub)

    print(maxAnswers)
