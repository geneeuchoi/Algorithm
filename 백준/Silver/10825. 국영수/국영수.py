N = int(input())
member_list = []

for _ in range(N):
    tmp = list(map(str, input().split(' ')))
    tmp[1], tmp[2], tmp[3] = int(tmp[1]), int(tmp[2]), int(tmp[3])
    member_list.append(tmp)

member_list.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(member_list[i][0])