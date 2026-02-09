
def solution(n):
    
    if n < 3: return n

    prev, curr = 1, 2
    
    for i in range(3, n+1):
        prev, curr = curr, (prev+curr)%1000000007
    
    return curr