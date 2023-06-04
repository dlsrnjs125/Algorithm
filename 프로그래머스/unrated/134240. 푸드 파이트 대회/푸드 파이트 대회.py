def solution(food):
    answer = ''
    
    for i in enumerate(food):
        cnt = i[1] // 2
        answer += str(i[0]) * cnt
    
    return answer + '0' + answer[::-1]