def solution(n, words):
    answer = [0, 0]
    words_set = set()
    words_set.add(words[0])

    for i in range(1, len(words)):
        last, present = words[i-1], words[i]
        last_word, present_word = last[-1], present[0]
        
        # 조건 1, 조건 2 확인
        if last_word != present_word or present in words_set:
            # n으로 딱 떨어지면 세트 맞지만
            # 떨어지지 않는다면 +1
            answer[0], answer[1] = (i+1)%n, (i+1)//n
            if (i+1)%n != 0: answer[1] += 1
            if (i+1)%n == 0: answer[0] += n
            
            break
        
        words_set.add(present)
        
            
    return answer