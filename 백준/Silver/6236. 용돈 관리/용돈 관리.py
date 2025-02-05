import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
budget = []
for _ in range(N):
    budget.append(int(sys.stdin.readline()))

def bs(start, end):
    k = end 
    while start <= end:
        mid = (start + end) // 2
        cnt = 1  
        having = mid

        for dayBudget in budget:
            if having < dayBudget:
                cnt += 1
                having = mid - dayBudget
            else:
                having -= dayBudget

        if cnt > M:
            start = mid + 1 
        else:
            k = mid 
            end = mid - 1 

    return k

start, end = max(budget), sum(budget)
print(bs(start, end))