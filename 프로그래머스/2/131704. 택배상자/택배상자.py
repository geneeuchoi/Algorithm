def solution(order):
    stack = []
    b_idx, o_idx = 1, 0
    
    while o_idx < len(order):
        
        if stack and order[o_idx] == stack[-1]: 
            stack.pop()
            o_idx += 1
            
        elif b_idx <= len(order):
            if b_idx == order[o_idx]:
                b_idx += 1
                o_idx += 1
            else:
                stack.append(b_idx)
                b_idx += 1
        else: break
    
    return o_idx