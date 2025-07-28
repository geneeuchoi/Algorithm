for _ in range(100):
    try:
        input_str = input()
        lower, upper, num, space = 0, 0, 0, 0

        for i in range(len(input_str)):
            if input_str[i].isupper(): 
                upper += 1
            elif input_str[i].islower(): 
                lower += 1
            elif input_str[i].isspace(): 
                space += 1
            else: 
                num += 1

        print(lower, upper, num, space)

    except:
        break