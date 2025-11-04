import sys
from sys import stdin

N = int(stdin.readline().rstrip())
words = set()

for _ in range(N):
    words.add(stdin.readline().rstrip())

words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words: print(word)