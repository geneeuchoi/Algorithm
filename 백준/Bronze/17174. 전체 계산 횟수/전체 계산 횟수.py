N, M = map(int, input().split(' '))

cnt = N

while N:
	N = N // M
	cnt += N


print(cnt)