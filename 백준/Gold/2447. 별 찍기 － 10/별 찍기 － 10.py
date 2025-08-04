from sys import stdin

def recursive(N, i_start, j_start):
    if N == 1: return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: 
                for x in range(i_start + i * (N // 3), i_start + (i+1) * (N // 3)):
                    for y in range(j_start + j * (N // 3), j_start + (j+1) * (N // 3)):
                        stars_list[x][y] = ' '
            else:
                recursive(N // 3, i_start + i * (N // 3), j_start + j * (N // 3))
         

N = int(stdin.readline().strip())
stars_list = [['*' for _ in range(N)] for _ in range(N)]

recursive(N, 0, 0)

for stars in stars_list:
    for elem in stars:
        print(elem, end = '')
    print()