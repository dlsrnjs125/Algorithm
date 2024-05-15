import math

def solution(n):
    answer = 0
    answer = (n * 6) // math.gcd(n, 6) // 6
    return answer