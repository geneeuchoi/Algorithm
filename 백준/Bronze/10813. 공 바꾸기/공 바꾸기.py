import sys

N, M = map(int, sys.stdin.readline().split(' '))
bucket = list(range(1, N+1))

for _ in range(M):
    i, j= map(int, sys.stdin.readline().split(' '))
    iValue, jValue = bucket[i-1], bucket[j-1]
    bucket[j-1] = iValue
    bucket[i-1] = jValue

for bucketIndex in range(len(bucket)):
    if bucketIndex != len(bucket):
        print(bucket[bucketIndex], end = " ")
    else:
        print(bucket[bucketIndex])