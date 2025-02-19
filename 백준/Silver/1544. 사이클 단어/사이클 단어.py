import sys

def rotate(word):
    return [word[i:] + word[:i] for i in range(len(word))]

cnt = int(sys.stdin.readline().rstrip())
uniqueWords = set()

for _ in range(cnt):
    word = sys.stdin.readline().rstrip()
    rotatedwords = rotate(word)
    found = False

    for rotated in rotatedwords:
        if rotated in uniqueWords:
            found = True
            break

    if not found:
        uniqueWords.add(word)

print(len(uniqueWords))