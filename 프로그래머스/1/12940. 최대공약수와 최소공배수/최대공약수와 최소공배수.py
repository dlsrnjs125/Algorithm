def solution(n, m):
    answer = []
    
    # 최대 공약수 구하기
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            answer.append(i)
            break
            
    # 최소 공배수 구하기 
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
            
    return answer