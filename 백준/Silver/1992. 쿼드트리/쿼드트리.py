from sys import stdin

def recursive(N, i_start, j_start):
    if N == 1:
        if video[i_start][j_start] == 0: print(0, end = '')
        else: print(1, end = '')
        return

    val = video[i_start][j_start]
    is_same = True
    for i in range(i_start, i_start + N):
        for j in range(j_start, j_start + N):
            if val != video[i][j]: 
                is_same = False
                break
        if not is_same: break

    if is_same:
        if val == 0: print(0, end = '')
        else: print(1, end = '')
        return

    print('(', end = '')
    for i in range(2):
        for j in range(2):
            recursive(N // 2, i_start + i * (N//2), j_start + j * (N//2))
    print(')', end = '')

N = int(stdin.readline().strip())
video = []
for _ in range(N):
    video.append(list(map(int, stdin.readline().strip())))

recursive(N, 0, 0)
