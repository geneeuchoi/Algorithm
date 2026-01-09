def solution(elements):
    
    double_elements = elements + elements
    sum_set = set()
    
    for i in range(len(elements)):
        tmp = 0
        for idx in range(i, i+len(elements)):
            tmp += double_elements[idx]
            sum_set.add(tmp)
    
    return len(sum_set)