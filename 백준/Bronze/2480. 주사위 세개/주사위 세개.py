dice = list(map(int, input().split(' ')))
dice.sort()

prize = 0

if dice[0] == dice[1] == dice[2]:
	prize = 10000 + dice[0] * 1000
elif dice[0] == dice[1]:
	prize = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
	prize = 1000 + dice[1] * 100
elif dice[0] == dice[2]:
	prize = 1000 + dice[0] * 100
else:
	prize = dice[2] * 100

print(prize)