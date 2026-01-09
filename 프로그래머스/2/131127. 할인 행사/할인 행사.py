def solution(want, number, discount):
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    answer = 0
    
    # 부르트포스
    for i in range(len(discount)-9):
        range_buy = dict()
        for j in range(i, i+10):
            item = discount[j]
            range_buy[item] = range_buy.get(item, 0) + 1
        is_match = True
        for key in want_dict:
            if range_buy.get(key, 0) < want_dict[key]:
                is_match = False
                break
        if is_match: answer += 1
            
            
    return answer