N = int(input())
num_list = []

for _ in range(N):
    tmp = list(map(int, input().split(' ')))
    num_list.append(tmp)

num_list.sort(key=lambda x:x[0])
num_list.sort(key=lambda x:x[1])


for i in range(len(num_list)):
    for j in range(2):
        print(num_list[i][j], end = ' ')
    print()
