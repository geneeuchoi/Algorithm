
input_str = input()
answer_str = ""

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(input_str)):
    tmp = input_str[i]
    if tmp.isalpha(): 
        if tmp.isupper():
            index = upper.index(tmp) + 13
            if index >= len(upper):
                index = index % len(upper)
            answer_str += upper[index]
        else:
            index = lower.index(tmp) + 13
            if index >= len(lower):
                index = index % len(lower)
            answer_str += lower[index]
    else: 
        answer_str += input_str[i]

print(answer_str)