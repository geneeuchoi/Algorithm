def solution(storey):
    if storey < 10:
        return min(storey, 10 - storey + 1) 
    
    remainder = storey % 10 # 뒷 자리 부터 확인
    return min(remainder + solution(storey // 10), 
               (10 - remainder) + solution(storey // 10 + 1))