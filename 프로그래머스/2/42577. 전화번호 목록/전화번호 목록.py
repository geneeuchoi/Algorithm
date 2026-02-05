def solution(phone_book):
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        prev, curr = phone_book[i-1], phone_book[i]
        if prev == curr[:len(prev)]: return False
    return True