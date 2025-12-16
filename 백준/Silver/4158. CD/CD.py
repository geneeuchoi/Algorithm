from sys import stdin

input = stdin.readline

while True:
    line = input().rstrip()
    if not line: break
    n, m = map(int, line.split())
    if n == 0 and m == 0: break

    sanguen = []
    for _ in range(n):
        sanguen.append(int(input().rstrip()))
    
    sunyoung = []
    for _ in range(m):
        sunyoung.append(int(input().rstrip()))

    cnt = 0
    i, j = 0, 0 

    while i < n and j < m:
        if sanguen[i] == sunyoung[j]:
            cnt += 1
            i += 1
            j += 1
        elif sanguen[i] < sunyoung[j]:
            i += 1
        else:
            j += 1
            
    print(cnt)