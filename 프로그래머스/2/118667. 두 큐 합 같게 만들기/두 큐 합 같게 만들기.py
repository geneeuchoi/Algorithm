from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    total = sum1 + sum2
    
    if total % 2:
        return -1
    
    half = total // 2
    if any(x > half for x in queue1 + queue2): return -1
    
    cnt = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    
    limit = len(queue1) * 4

    while sum1 != sum2:
        if cnt > limit:
            return -1
        
        if sum1 > sum2: 
            elem = queue1.popleft()
            queue2.append(elem)
            sum1-=elem
            sum2+=elem
        else:
            elem = queue2.popleft()
            queue1.append(elem)
            sum2-=elem
            sum1+=elem
        cnt += 1
    return cnt