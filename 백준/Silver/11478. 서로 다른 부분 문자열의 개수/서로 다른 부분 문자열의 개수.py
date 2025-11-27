from sys import stdin

s = stdin.readline().rstrip()
diff = set()
idx = 1

while(idx<=len(s)):
    for start in range(len(s)):
        end = start + idx
        if end <= len(s):
            diff.add(s[start:end])
        else: break
    idx += 1

print(len(diff))
