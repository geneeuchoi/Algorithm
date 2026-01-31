from collections import deque

def solution(priorities, location):
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    answer = 0

    while queue:
        curr = queue.popleft()
        
        if any(curr[0] < p[0] for p in queue):
            queue.append(curr)
        else:
            answer += 1
            if curr[1] == location:
                return answer