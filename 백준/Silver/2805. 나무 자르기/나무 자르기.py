import sys
  
# 나무의 수 N. 집으로 가져가려는 나무의 길이 M
N, M = map(int, input().split(' '))

# 집 앞 나무들의 길이
trees = list(map(int, input().split(' ')))

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
def bs(trees, M):
    left, right = 0, max(trees) 

    while left + 1 < right:
        mid = (left + right) // 2
        length = 0 
        for tree in trees:
            if tree - mid > 0:
                length += tree - mid
        if length >= M:
            left = mid 
        else:
            right = mid  
    return right-1
print(bs(trees, M))