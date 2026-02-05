def solution(numbers, target):
    answer = 0
    n = len(numbers)
    # 완탐 -> dfs. 재귀
    def dfs(idx, current_sum):
        nonlocal answer
        
        if idx == n:
            if current_sum == target: answer += 1
            return
    
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])
    
    dfs(0, 0)
    return answer
    