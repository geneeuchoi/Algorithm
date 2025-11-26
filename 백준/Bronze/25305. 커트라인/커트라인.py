from sys import stdin

N, k = map(int, stdin.readline().rstrip().split(' '))
score = list(map(int, stdin.readline().rstrip().split(' ')))
score.sort()
print(score[-k])