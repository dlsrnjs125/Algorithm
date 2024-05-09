import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    num = numer1*denom2 + numer2*denom1
    gcd = math.gcd(denom, num)
    answer = [num/gcd, denom/gcd]
    return answer