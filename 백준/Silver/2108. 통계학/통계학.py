from sys import stdin

n = int(stdin.readline().rstrip())
nums = []
nums_set = set()
nums_dict = dict()
nums_sum = 0

for _ in range(n):
    tmp = int(stdin.readline().rstrip())
    nums_sum += tmp
    nums.append(tmp)
    nums_set.add(tmp)
    nums_dict[tmp] = 0

# 산술 평균
avg = nums_sum/n
print(int(round(avg, 0)))

# 중앙값
nums.sort()
print(nums[(n-1)//2])

# 최빈값
# 최빈값 여러개일 때에는 두번째로 작은 값
frequent_nums = []
max_cnt, max_num = 0, 0

for elem in nums:
    nums_dict[elem] += 1

for elem in nums_set:
    cnt = nums_dict[elem]
    if cnt > max_cnt: 
        max_num = elem
        max_cnt = cnt

for elem in nums_set:
    cnt = nums_dict[elem]
    if cnt == max_cnt:
        frequent_nums.append(elem)

frequent_nums.sort()
if len(frequent_nums) > 1:
    print(frequent_nums[1])
else:
    print(max_num)

# 범위
print(nums[n-1]-nums[0])