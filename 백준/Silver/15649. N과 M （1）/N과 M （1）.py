
# 1부터 n까지의 자연수를 가진 집합이 주어진다.
# m개의 원소를 가진 수열을 구하시오
n, m = map(int, input().split(' '))
visited = [0 for _ in range(n+1)]
seq = []

def bt(k):
    if k == m:
        for i in seq:
            print(i, end = ' ')
        print()
        return
    

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            seq.append(i)
            bt(k+1)
            visited[i] = 0
            seq.pop()




bt(0)