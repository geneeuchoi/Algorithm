def solution(players, m, k):
    servers = [0 for _ in range(24)]
    answer = 0
    
    for i in range(24):
        need = players[i] // m
        if servers[i] < need:
            add = need - servers[i]
            answer += add
            for j in range(i, min(i+k, 24)):
                servers[j] += add
    return answer