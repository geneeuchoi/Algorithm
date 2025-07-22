import sys

def push(queue, n):
    queue.append(n)

def pop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.pop(0)

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


N = int(sys.stdin.readline().strip())
queue = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command == 'pop': pop(queue)
    elif command == 'size': size(queue)
    elif command == 'empty': empty(queue)
    elif command == 'front': front(queue)
    elif command == 'back': back(queue)
    else: push(queue, int(command[5:]))