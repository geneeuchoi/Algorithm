from collections import deque

def check(queue):
    stack = []
    braces = {'(': ')', '{': '}', '[': ']'}
    
    for char in queue:
        if char in braces: stack.append(char)
        else:
            if not stack or braces[stack.pop()] != char: return False

    return len(stack) == 0
    
def solution(s):
    queue = deque(s)

    answer = 0
    for _ in range(len(s)):
        if check(queue): answer += 1
        curr = queue.popleft()
        queue.append(curr)
    
    return answer