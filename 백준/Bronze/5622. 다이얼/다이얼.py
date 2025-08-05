from sys import stdin


phone_number = list(stdin.readline().strip())

alphabet = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

time = 0

for number in phone_number:
    for i in range(len(alphabet)):
        for j in range(len(alphabet[i])):
            if alphabet[i][j] == number:
                time += i + 3
                break
print(time)

