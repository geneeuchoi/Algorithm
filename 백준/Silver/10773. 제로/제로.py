from sys import stdin

K = int(stdin.readline().rstrip())

money_list = []
money_sum = 0

for _ in range(K):
    money = int(stdin.readline().rstrip())
    if money == 0 and len(money_list) > 0: money_list.pop(len(money_list)-1)
    else: money_list.append(money)

for money in money_list:
    money_sum += money

print(money_sum)