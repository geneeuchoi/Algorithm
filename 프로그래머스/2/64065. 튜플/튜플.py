def solution(s):
    # 1 -> 12 -> 123 -> 1234
    s = s.strip("{}")
    s = list(s.split("},{"))
    
    frequency = dict()
    for item in s:
        tmp = list(map(int, item.split(",")))
        for tmp_i in tmp:
            d = frequency.get(tmp_i, 0)
            frequency[tmp_i] = d + 1

    s_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for x in s_frequency:
        answer.append(x[0])
    return answer