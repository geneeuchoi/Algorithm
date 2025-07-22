import sys

N = int(sys.stdin.readline().strip())
card_dict = dict()

for _ in range(N):
    card = int(sys.stdin.readline().strip())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

card_list = list(card_dict.items())
card_list.sort(key = lambda x: (x[1], -x[0]))
print(card_list[len(card_list)-1][0])