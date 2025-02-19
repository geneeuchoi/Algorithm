import sys

burger = []
burger.append(int(sys.stdin.readline().rstrip()))
burger.append(int(sys.stdin.readline().rstrip()))
burger.append(int(sys.stdin.readline().rstrip()))
burger.sort()

bevarage = []
bevarage.append(int(sys.stdin.readline().rstrip()))
bevarage.append(int(sys.stdin.readline().rstrip()))
bevarage.sort()

print(burger[0] + bevarage[0] - 50)