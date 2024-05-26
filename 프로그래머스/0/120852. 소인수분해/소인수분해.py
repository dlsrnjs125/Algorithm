def solution(n):
    answer = []
    k = 2
    
    while k <= n:
        if n % k == 0:
            if k not in answer:
                answer.append(k)
            n //= k
        else:
            k += 1
    
    return answer