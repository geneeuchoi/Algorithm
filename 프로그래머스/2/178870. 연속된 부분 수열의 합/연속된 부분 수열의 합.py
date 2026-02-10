def solution(sequence, k):
    left, current_sum = 0, 0
    min_len = float('inf')
    answer = [0, 0]

    for right in range(len(sequence)):
        current_sum += sequence[right]
        
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1
            
        if current_sum == k:
            current_length = right - left
            if current_length < min_len:
                min_len = current_length
                answer = [left, right]
            
            
    return answer