def solution(a, b, n):
    answer = 0
    
    while n >= a:
        cnt = n // a # 새로 받은 콜라 개수
        answer += cnt * b
        n = (cnt * b) + (n % a)
        
    return answer