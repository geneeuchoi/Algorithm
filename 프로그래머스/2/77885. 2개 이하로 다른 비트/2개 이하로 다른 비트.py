def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0: answer.append(num+1)
        else: 
            bit = ~num & (num + 1)
            answer.append(num + bit - (bit // 2))
    return answer