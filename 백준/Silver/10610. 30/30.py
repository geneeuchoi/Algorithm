from sys import stdin

num_list = list(stdin.readline().strip())

if '0' not in num_list:
    print(-1)
else:
    total = sum(map(int, num_list))
    if total % 3 != 0:
        print(-1)
    else:
        num_list.sort(reverse=True)
        print(''.join(num_list))