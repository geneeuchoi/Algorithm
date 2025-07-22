import sys

def push_front(deque, n):
    deque.insert(0, n)

def push_back(deque, n):
    deque.append(n)

def pop_front(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])
        deque.pop(0)

def pop_back(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])
        deque.pop(-1)

def size(deque):
    print(len(deque))

def empty(deque):
    if len(deque) == 0:
        print(1)
    else:
        print(0)

def front(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])

def back(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])


N = int(sys.stdin.readline().strip())
deque = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command == 'pop_front': pop_front(deque)
    elif command == 'pop_back': pop_back(deque)
    elif command == 'size': size(deque)
    elif command == 'empty': empty(deque)
    elif command == 'front': front(deque)
    elif command == 'back': back(deque)
    elif command[0:9] == 'push_back': push_back(deque, int(command[10:]))
    else: push_front(deque, int(command[11:]))