from sys import stdin

def tw(cards):
    front = 0 
    rear = len(cards) 

    while rear - front > 1:
        front += 1 
        cards.append(cards[front])
        front += 1
        rear += 1 

    return cards[front]

N = int(stdin.readline().rstrip())
cards = [i for i in range(1, N + 1)]
print(tw(cards))
