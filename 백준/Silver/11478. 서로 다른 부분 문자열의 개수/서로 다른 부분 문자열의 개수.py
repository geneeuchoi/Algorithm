from sys import stdin

s = stdin.readline().rstrip()
diff = set()

for idx in range(1, len(s)+1):
    for start in range(len(s)):
        end = start + idx
        if end <= len(s):
            diff.add(s[start:end])

print(len(diff))
