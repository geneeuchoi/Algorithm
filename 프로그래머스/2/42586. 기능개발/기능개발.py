def solution(progresses, speeds):
    deploy = []
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        left_d = left // speeds[i]
        if left % speeds[i] > 0: left_d += 1
        deploy.append(left_d)
    
    print(deploy)
    answer_arr, k = [], 0
    answer_arr = []
    k = 0
    
    while k < len(deploy):
        prev = deploy[k]
        count = 1
        
        j = k + 1
        while j < len(deploy) and prev >= deploy[j]:
            count += 1
            j += 1
            
        answer_arr.append(count)
        k = j

    return answer_arr