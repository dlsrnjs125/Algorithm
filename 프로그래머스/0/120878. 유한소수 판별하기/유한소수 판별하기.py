from math import gcd

def solution(a, b):
    answer = 0
    b = b / gcd(a, b)
    
    for i in [2, 5]:
        while not b % i:
            b //= i
    
    if b == 1:
        answer = 1
    else:
        answer = 2
    
    return answer