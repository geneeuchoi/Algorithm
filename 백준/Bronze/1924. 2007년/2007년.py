day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

input_month, input_day = map(int, input().split(' '))
day_sum = 0;

for i in range(0, input_month-1):
    day_sum += month_day[i]
day_sum += input_day

print(day[day_sum % 7])