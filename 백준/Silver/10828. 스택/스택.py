import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == 'top':
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif command == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        num = int(command[5:])
        stack.append(num)