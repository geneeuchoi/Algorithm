def combination(cloth_map):
    vals = cloth_map.values()
    sum = 1
    for val in vals:
        sum *= val + 1
    return sum-1

def solution(clothes):
    cloth_map = dict()
    
    for cloth in clothes:
        cloth_map[cloth[1]] = cloth_map.get(cloth[1], 0) + 1
    
    return combination(cloth_map)