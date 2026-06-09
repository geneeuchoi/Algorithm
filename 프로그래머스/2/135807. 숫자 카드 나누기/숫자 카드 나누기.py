def get_divisors(n, arr):
    for i in range(2, n//2+1):
        if n % i == 0: arr.append(i)
    return arr

def solution(arrayA, arrayB):
    minA, minB = min(arrayA), min(arrayB)
    gcdA, gcdB = get_divisors(minA, [minA]), get_divisors(minB, [minB])
    allGcd = set(gcdA + gcdB)
    
    maxGcd = 0
    for gcd in allGcd:
        case_A = [x % gcd for x in arrayA]
        case_B = [x % gcd for x in arrayB]
        
        is_A_all_zero = all(x == 0 for x in case_A)
        is_B_all_zero = all(x == 0 for x in case_B)

        is_A_has_zero = any(x == 0 for x in case_A)
        is_B_has_zero = any(x == 0 for x in case_B)

        if (is_A_all_zero and not is_B_has_zero) or (is_B_all_zero and not is_A_has_zero):
            if gcd > maxGcd:
                maxGcd = gcd


    return maxGcd

