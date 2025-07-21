N = int(input())

for i in range(N-1):
    print(' ' * (N - i - 1), end = '')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
print('*' * (N * 2 - 1))