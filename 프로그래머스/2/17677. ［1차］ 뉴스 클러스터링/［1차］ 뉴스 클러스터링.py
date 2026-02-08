from collections import Counter

def multiple_set(strs):
    answer = []
    for i in range(len(strs)-1):
        s = strs[i:i+2]
        if s.isalpha(): answer.append(s)
    return answer

def solution(str1, str2):
    l1_s, l2_s = multiple_set(str1.lower()), multiple_set(str2.lower())
    l1_m, l2_m= Counter(l1_s), Counter(l2_s)
    
    inter = 0
    for l1_k, l1_v in l1_m.items():
        inter += min(l1_v, l2_m.get(l1_k, 0))
    
    union = 0
    all_keys = set(l1_m.keys()) | set(l2_m.keys())
    for k in all_keys:
        union += max(l1_m.get(k, 0), l2_m.get(k, 0))
        
    if union == 0: return 65536
    return int((inter/union)*65536)