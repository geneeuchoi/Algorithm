N = int(input())
member_list = []

for _ in range(N):
    tmp = list(map(str, input().split(' ')))
    tmp[0] = int(tmp[0])
    member_list.append(tmp)

member_list.sort(key=lambda x:x[0])

for i in range(N):
    for j in range(2):
        print(member_list[i][j], end = ' ')
    print()
