def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        cnt = get_count(i, limit, power)
        answer += cnt
    
    return answer

# 약수 개수
def get_count(n, limit, power):
    count = 0
    
    for i in range(1, int(n**(1/2)) + 1): # 제곱근만큼만 반복
        if n % i == 0:
            if i == n // i: # 제곱근일 경우
                count += 1
            else:
                count += 2
        if count > limit: # limit 개수를 넘어가면 power로 return
            return power
            
    return count