from sys import stdin

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer


def combination(n):
    answer = 0
    for i in range(n//3 + 1):
        for j in range(n - (i * 3) + 1):
            for k in range(n - (i * 3) - (j * 2) + 1):
                if i * 3 + j * 2 + k == n:
                    answer += factorial(i + j + k) // (factorial(i) * factorial(j) * factorial(k))
    return answer

T = int(stdin.readline().strip())

for _ in range(T):
    n = int(stdin.readline().strip())
    print(combination(n))