def solution(citations):
    citations.sort()
    left, right= 0, len(citations)
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        count = 0
        
        for x in citations:
            if x >= mid: count += 1

        if count >= mid:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    
    return answer