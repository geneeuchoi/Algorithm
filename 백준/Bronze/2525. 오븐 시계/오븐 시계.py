h, m = map(int, input().split(' '))
cookTime = int(input())

m += cookTime
if m >= 60:
	h +=  m // 60
	m = m % 60

if h >= 24:
	h -= 24

print(h, m)