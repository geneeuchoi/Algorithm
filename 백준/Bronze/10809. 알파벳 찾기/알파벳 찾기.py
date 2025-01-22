import sys

S = sys.stdin.readline().rstrip()
alphabet = [-1 for _ in range(26)]

for i in range(len(S)):
    if alphabet[ord(S[i])-97] == -1:
        alphabet[ord(S[i])-97] = i

for elem in alphabet:
    print(elem, end = " ")