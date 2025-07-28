input_str = input()
str_list = []
for i in range(len(input_str)):
    str_list.append(input_str[i:])

str_list.sort()
for s in str_list:
    print(s)