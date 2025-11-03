import sys
from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(" "))
cards = list(map(int, stdin.readline().rstrip().split(" ")))
card_sum = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp < M: card_sum.append(tmp)
            elif tmp == M: 
                print(tmp)
                exit(0)

print(max(card_sum))
