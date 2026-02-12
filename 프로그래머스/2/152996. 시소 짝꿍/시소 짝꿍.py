from collections import Counter

def solution(weights):
    counter = Counter(weights)
    unique_w = sorted(counter.keys())
    answer = 0
    
    for current in unique_w:
        n = counter[current]
        if n > 1: answer += n * (n - 1) // 2

        if counter[current*(3/2)]:
            answer += counter[current] * counter[current*(3/2)]
        if counter[current*2]:
            answer += counter[current] * counter[current*2]
        if counter[current*(4/3)]:
            answer += counter[current] * counter[current*(4/3)]
        
        
    return answer