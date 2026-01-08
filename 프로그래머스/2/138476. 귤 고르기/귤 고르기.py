def solution(k, tangerine):
    tan_dict = dict()
    
    for tan in tangerine:
        tan_dict[tan] = tan_dict.get(tan, 0)+1
    
    tan_list = list(tan_dict.items())
    tan_list.sort(key = lambda x: -x[1])
    target, answer = k, 0
    
    for tan in tan_list:
        answer += 1
        if tan[1] >= target: break
        else: target -= tan[1]
            
    return answer