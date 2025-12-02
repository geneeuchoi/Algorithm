
import sys
sys.setrecursionlimit(10000)

def solve():
    n = int(sys.stdin.readline())
    
    v1 = [False] * n              # 열(Col) 체크
    v2 = [False] * (2 * n)        # 대각선 / 체크 (r + c)
    v3 = [False] * (2 * n)        # 대각선 \ 체크 (r - c + n - 1)
    
    count = 0

    def dfs(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if not v1[col] and not v2[row + col] and not v3[row - col + n - 1]:
                
                v1[col] = True
                v2[row + col] = True
                v3[row - col + n - 1] = True
                
                dfs(row + 1)
                
                v1[col] = False
                v2[row + col] = False
                v3[row - col + n - 1] = False

    dfs(0)
    print(count)

solve()