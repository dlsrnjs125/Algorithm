def solution(array, height):
    answer = 0
    tmp = sorted(array, reverse=True)
    
    for i in tmp:
        if i > height:
            answer += 1
    return answer