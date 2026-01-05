def solution(s):
    stack = []
    if s[0] == ")" or len(s) == 0:
        return False
    
    for elem in s:
        if elem == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            stack.pop()
            
    
    if len(stack) != 0: 
        return False
    

    return True