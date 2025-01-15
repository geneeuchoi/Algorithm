N = int(input())
codeList = list(map(int, input().split(' ')))
decodedStrList= list(input())

decodingElemList = []

for code in codeList:
	if code == 0:
		decodingElemList.append(" ")
	elif 1 <= code <= 26:
		decodingElemList.append(chr(code+64))
	else:
		decodingElemList.append(chr(code+70))

decodedStrList.sort()
decodingElemList.sort()

if decodedStrList == decodingElemList:
	print("y")
else:
	print("n")