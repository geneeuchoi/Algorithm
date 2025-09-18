from sys import stdin

N, game = map(str, stdin.readline().strip().split(' '))
player_len = 0
if game == 'Y': player_len = 1
elif game == 'F': player_len = 2
else: player_len = 3

player = set()
for _ in range(int(N)):
	player.add(stdin.readline().strip())

print(len(player)//player_len)