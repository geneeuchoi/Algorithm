import sys
input = sys.stdin.readline

N = int(input())
NList = list(map(int, input().split()))
NList.sort()

M = int(input())
MList = list(map(int, input().split()))

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

for x in MList:
    if binary_search(NList, x):
        print(1)
    else:
        print(0)
