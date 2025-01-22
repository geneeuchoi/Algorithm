import sys

studentList = [0 for _ in range(30)]

for _ in range(28):
    i = int(sys.stdin.readline())
    studentList[i-1] = 1

absentStudent = []
for studentNum in range(30):
    if studentList[studentNum] == 0:
        absentStudent.append(studentNum+1)

absentStudent.sort()
print(absentStudent[0])
print(absentStudent[1])
