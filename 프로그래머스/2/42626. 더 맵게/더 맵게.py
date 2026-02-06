import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2: return -1
        
        answer += 1
        food1, food2 = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2 * 2)
    
    return answer