def solution(left, right):
    answer = 0
    # 약수 개수 홀수 -> 제곱수
    
    for i in range(left, right+1):
        if i**0.5 - int(i**0.5) == 0: # 제곱수 판별 -> 개수 : 홀수
            answer -= i
        else:
            answer += i
    
    return answer