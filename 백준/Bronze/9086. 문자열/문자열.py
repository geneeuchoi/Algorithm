import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    S = sys.stdin.readline().rstrip()
    print(S[0] + S[len(S)-1])