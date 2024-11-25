n, s = map(int, input().split())
seq = list(map(int, input().split()))

# 크기가 양수(공집합이 아님)인 부분수열 중에서 합이 s가 되는 경우의 수
count = 0

def find_subsequences(k, seqSum):
    global count

    # 모든 원소를 검사한 경우
    if k == n:
        # 합이 s인 경우 카운트 증가
        count += (seqSum == s)
        return

    # 현재 원소를 포함하지 않는 경우
    find_subsequences(k + 1, seqSum)

    # 현재 원소를 포함하는 경우
    find_subsequences(k + 1, seqSum + seq[k])

find_subsequences(0, 0)

# s가 0인 경우 공집합을 제외
if s == 0:
    count -= 1

print(count)
