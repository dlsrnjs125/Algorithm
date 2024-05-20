from math import factorial

def solution(balls, share):
    answer = 0
    n = factorial(balls) # n!
    m = factorial(share) # m!
    
    answer = n/(factorial(balls-share) * m)
    return answer