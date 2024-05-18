def solution(n, k):
    answer = 0
    free = n // 10
    
    answer = n * 12000 + (k-free) * 2000
    return answer