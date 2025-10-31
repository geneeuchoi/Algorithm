import sys
from sys import stdin

# 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성

N = int(stdin.readline().strip())
step, ran = 0, 1

for i in range(1, 100000000):
    if N <= ran: break
    ran += i * 6
    step += 1
    
print(step+1)