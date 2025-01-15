def getbinary(n):
    if n == 0:
        return "0000"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    if len(binary) < 4:
        for _ in range(4 - len(binary)):
            binary = "0" + binary

    return binary[-4:]

num1 = int(input())
num2 = int(input())
num3 = int(input())

binaryString = getbinary(num1) + getbinary(num2) + getbinary(num3)

password = 0

for i in range(len(binaryString)):
    password += (2 ** (len(binaryString) - 1 - i)) * int(binaryString[i])

password = str(password)

if len(password) < 4:
        for _ in range(4 - len(password)):
            password = "0" + password

print(password)