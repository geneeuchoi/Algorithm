from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5

    cache = deque(maxlen = cacheSize)
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

    return answer