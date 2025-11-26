from sys import stdin

N = int(stdin.readline().rstrip())
cordinate_not = list(map(int, stdin.readline().rstrip().split(" ")))
cordinate = sorted(cordinate_not)
cordinate_dict = dict()
doubled, minx, left = 0, cordinate[0], cordinate[0]
cordinate_dict[cordinate[0]] = 0
for i in range(1, len(cordinate)):
    if cordinate[i] == left:
        doubled += 1
    else:
        left = cordinate[i]
    cordinate_dict[cordinate[i]] = i - doubled

for elem in cordinate_not:
    print(cordinate_dict[elem], end = " ")