def solution(order):
    answer = 0
    
    for i in str(order):
        if i == '3':
            answer += 1
        elif i == '6':
            answer += 1
        elif i == '9':
            answer += 1
    return answer