import sys

N, M = map(int, sys.stdin.readline().split(' '))
bucket = [0 for _ in range(N)] 

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split(' '))
    for index in range(i-1, j):
        bucket[index] = int(k)

for bucketIndex in range(len(bucket)):
    if bucketIndex != len(bucket):
        print(bucket[bucketIndex], end = " ")
    else:
        print(bucket[bucketIndex])
