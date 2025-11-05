import sys
from sys import stdin

# ======입력부======
N, K = map(int, stdin.readline().rstrip().split(" "))
circle = [i for i in range(1, N+1)]
answer = []

# ======K보다 클 때까지======
while len(circle) >= K:
    tmp = circle[K-1]
    circle.pop(K-1)
    answer.append(tmp)

    for _ in range(K-1):
        tmp = circle[0]
        circle.append(tmp)
        circle.pop(0)

# ======K보다 작을 때======
idx = 0
while circle:
    idx = (idx + K - 1) % len(circle)
    answer.append(circle.pop(idx))

# ======출력부======
print("<", end="")
for i in range(N-1):
    print(answer[i], end=", ")
print(f"{answer[N-1]}>")
