cho = list(map(float, input().split(' ')))
han = list(map(float, input().split(' ')))


# 차, 포, 마, 상, 사, 졸
jang = [13, 7, 5, 3, 3, 2]

choSum, hanSum = 0, 0

for i in range(6):
	choSum += cho[i] * jang[i]
	hanSum += han[i] * jang[i] 

if choSum > hanSum + 1.5:
	print("cocjr0208")
else:
	print("ekwoo")