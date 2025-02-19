import sys

yakCnt = int(sys.stdin.readline().rstrip())
realYak = list(map(int, sys.stdin.readline().rstrip().split(' ')))
realYak.sort()
# 진짜약수 개수가 짝수다 - 짝 맞춰서 곱한다
# 진짜약수 개수가 홀수다 - 가운데 애 두번 곱한다.

answer = 0
if yakCnt % 2 == 0:
    answer = realYak[0] * realYak[yakCnt-1]
else:
    answer = realYak[yakCnt // 2] ** 2
print(answer)
