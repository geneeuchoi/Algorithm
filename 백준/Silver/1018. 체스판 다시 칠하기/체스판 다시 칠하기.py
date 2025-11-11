import sys
from sys import stdin


def check(board):
    repainting1, repainting2 = 0, 0

    # 왼쪽 위가 B일 때
    for i in range(8):
        for j in range(8):
            if i%2 == 0:
                if (j%2 == 0 and board[i][j] != "B") or (j%2 == 1 and board[i][j] != "W"): repainting1 += 1
            else:
                if (j%2 == 0 and board[i][j] != "W") or (j%2 == 1 and board[i][j] != "B"): repainting1 += 1

    # 왼쪽 위가 W일 때
    for i in range(8):
        for j in range(8):
            if i%2 == 0:
                if (j%2 == 0 and board[i][j] != "W") or (j%2 == 1 and board[i][j] != "B"): repainting2 += 1
            else:
                if (j%2 == 0 and board[i][j] != "B") or (j%2 == 1 and board[i][j] != "W"): repainting2 += 1

    return min(repainting1, repainting2)

N, M = map(int, stdin.readline().rstrip().split(" "))
board = []
for _ in range(N):
    board.append(list(stdin.readline().rstrip()))

repainting = []
for i in range(N-7):
    for j in range(M-7):
        sub_board = [row[j:j+8] for row in board[i:i+8]]
        repainting.append(check(sub_board))


repainting.sort()
print(repainting[0])


