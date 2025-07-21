N = int(input())

for i in range(N):
    print(' ' * (N - i - 1), end = '')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()