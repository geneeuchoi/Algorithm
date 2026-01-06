def check_one(nums):
    one_cnt = 0
    # 부르트포스로 풀었지만, 1을 더 빠르게 체크할 수 있는 법은 없을까?
    for elem in nums:
        if elem == 1: one_cnt += 1
    return one_cnt

def binary(n):
    nums = []
    while(True):
        if n == 1 or n == 0: 
            nums.append(n)
            return nums
        nums.append(n % 2)
        n = n // 2

def binary_check(n):
    # 먼저 이진수로 변환한다.
    # 이진수 변환법: 2로 나누고, 나머지를 하나씩 붙인다.
    nums = binary(n)
    
    # 이진수의 1의 개수를 체크한다.
    cnt = check_one(nums)
    return cnt
    
def solution(n):
    n_cnt = binary_check(n)
    
    while(True):
        target = n+1
        target_cnt = binary_check(target)
        if n_cnt == target_cnt: return target
        n = target