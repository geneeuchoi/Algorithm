def solution(n):
    answer = 0
    start, end, curr_sum = 1, 1, 1
    
    while start <= n:
        if curr_sum < n:
            end += 1
            curr_sum += end
        elif curr_sum == n:
            answer += 1
            curr_sum -= start
            start += 1
        else:
            curr_sum -= start
            start += 1
    return answer