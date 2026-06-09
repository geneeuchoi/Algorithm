def solution(skill, skill_trees):
    skill_list = list(skill)
    skill_dict = dict()
    for i in range(len(skill_list)):
        skill_dict[skill_list[i]] = i
    
    answer = 0
    
    for tree in skill_trees:
        tree_list = list(tree)
        prev = -1
        flag = True
        
        for t in range(len(tree_list)):
            t_val = skill_dict.get(tree_list[t], -1)
            if t_val == -1: continue
            
            if t_val != prev+1:
                flag = False
                break
                
            prev = t_val
        if flag: answer += 1

    return answer