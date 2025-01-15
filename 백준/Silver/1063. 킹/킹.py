king, rock, N = input().split(' ')
kingPlace = [int(king[1])-1, ord(king[0])-65]
rockPlace = [int(rock[1])-1, ord(rock[0])-65]

moveDict = {"R": [0, 1], "L": [0, -1], "B": [-1, 0], "T": [1, 0],
"RT": [1, 1], "LT": [1, -1], "RB": [-1, 1] , "LB": [-1, -1]}

for _ in range(int(N)):
	move = input()

	movedKingPlaceX = kingPlace[0] + moveDict[move][0]
	movedKingPlaceY = kingPlace[1] + moveDict[move][1]

	if 0<= movedKingPlaceX<= 7 and 0<= movedKingPlaceY<= 7:
		# 돌 체크(돌 위치 == 움직인 킹 위치?)
		if(movedKingPlaceX == rockPlace[0]) and (movedKingPlaceY == rockPlace[1]):
			movedRockPlaceX = rockPlace[0] + moveDict[move][0]
			movedRockPlaceY = rockPlace[1] + moveDict[move][1]
			# 움직인 돌이 체스판 안에 있는지 확인
			if 0<= movedRockPlaceX<= 7 and 0<= movedRockPlaceY<= 7:
				 rockPlace[0] = movedRockPlaceX
				 rockPlace[1] = movedRockPlaceY
				 kingPlace[0] = movedKingPlaceX
				 kingPlace[1] = movedKingPlaceY
		else:
			kingPlace[0] = movedKingPlaceX
			kingPlace[1] = movedKingPlaceY


print(chr(kingPlace[1]+65)+str(kingPlace[0]+1))
print(chr(rockPlace[1]+65)+str(rockPlace[0]+1))