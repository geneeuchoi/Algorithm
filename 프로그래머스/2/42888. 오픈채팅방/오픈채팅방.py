def solution(record):
    
    answer = []
    # uid로 해쉬 만들어서 값 업데이트
    # enter => 님이 들어왔습니다.
    # leave => 님이 나갔습니다.
    # Change => 리스트에 담지 않는다.
    
    nicknames = dict()
    for message in record:
        m_list = message.split()
        state = m_list[0]
        
        if state == "Enter" or state == "Change":
            user_id, nickname = m_list[1], m_list[2]
            nicknames[user_id] = nickname
        
    answer = []
    for message in record:
        m_list = message.split()
        state = m_list[0]
        if state == "Enter":
            user_id = m_list[1]
            answer.append(nicknames[user_id] + "님이 들어왔습니다.")
        
        if state == "Leave":
            user_id = m_list[1]
            answer.append(nicknames[user_id] + "님이 나갔습니다.")
        
    return answer