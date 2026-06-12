def solution(array):
    index, value = 0, 0
    max_v = 0
    for i, e in enumerate(array):
        if e > max_v:
            index, value = i, e
            max_v = e
            
    answer = [value, index]
    return answer