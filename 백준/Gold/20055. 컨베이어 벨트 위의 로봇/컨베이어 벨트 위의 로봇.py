from sys import stdin

N, K = map(int, stdin.readline().strip().split(' '))
conveyer = list(map(int, stdin.readline().strip().split(' ')))
robot = [0 for _ in range(N)]
zero = 0
step = 0

while zero < K:
    step += 1

    # 회전
    conveyer = [conveyer[-1]] + conveyer[:-1]
    robot = [0] + robot[:-1]
    robot[-1] = 0

    # 로봇 이동
    for i in range(N-2, -1, -1):
        # 올리기: 로봇이 없고, 컨베이어가 1이상
        if robot[i] and not robot[i+1] and conveyer[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            conveyer[i+1] -= 1
            if conveyer[i+1] == 0:
                zero += 1
    robot[-1] = 0 

    # 올리기
    if conveyer[0] > 0 and not robot[0]:
        robot[0] = 1
        conveyer[0] -= 1
        if conveyer[0] == 0:
            zero += 1


print(step)