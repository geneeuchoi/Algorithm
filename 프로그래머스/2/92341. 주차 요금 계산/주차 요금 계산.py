import math

def solution(fees, records):
    parking = dict()
    cum = dict()
    
    for record in records:
        clock, number, state = record[:5], record[6:10], record[11:]
        if state == "IN": parking[number] = clock
        if state == "OUT": 
            IN_clock = parking.pop(number)
            IN_hour, IN_min, OUT_hour, OUT_min = int(IN_clock[:2]), int(IN_clock[3:]), int(clock[:2]), int(clock[3:])
            total = (OUT_hour - IN_hour) * 60 + (OUT_min - IN_min)
            cum[number] = cum.get(number, 0) + total
    
    if any(parking):
        for number in parking:
            IN_clock = parking[number]
            IN_hour, IN_min, OUT_hour, OUT_min = int(IN_clock[:2]), int(IN_clock[3:]), 23, 59
            total = (OUT_hour - IN_hour) * 60 + (OUT_min - IN_min)
            cum[number] = cum.get(number, 0) + total
    
    b_hour, b_fee, e_hour, e_fee = fees[0], fees[1], fees[2], fees[3]
    answer_d = dict()
    for number in cum:
        total_clock = cum[number]

        if total_clock <= b_hour: total_fee = b_fee
        else: total_fee = b_fee + math.ceil((total_clock - b_hour) / e_hour) * e_fee

        answer_d[number] = total_fee
    
    answer_key = sorted(answer_d)
    answer = []
    for key in answer_key:
        answer.append(answer_d.get(key, 0))
    return answer