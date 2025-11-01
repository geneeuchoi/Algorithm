import sys
from sys import stdin

isbn = stdin.readline().strip()
sum_isbn, star_w, check = 0, 0, int(isbn[12])

for i in range(len(isbn)-1):
    if isbn[i] != "*":
        if i % 2 == 0: sum_isbn += int(isbn[i])
        else: sum_isbn += int(isbn[i]) * 3
    else: 
        if i % 2 == 0: star_w = 1
        else: star_w = 3

for i in range(0, 10):
    if check == 0 and (sum_isbn + star_w * i) % 10 ==0 :
        print(i)
    elif check != 0 and check == 10 - (sum_isbn + star_w * i) % 10:
        print(i)

