from collections import Counter

def solution(topping):
    answer = 0
    bro_map, cheolsu_set = Counter(topping), set()
    bro_nums = len(bro_map)
    
    for t in topping: 
        cheolsu_set.add(t)
        bro_map[t] -= 1
        if bro_map[t] == 0:
            bro_nums -= 1
        
        if len(cheolsu_set) == bro_nums: answer += 1
        elif len(cheolsu_set) > bro_nums: break
    
    return answer