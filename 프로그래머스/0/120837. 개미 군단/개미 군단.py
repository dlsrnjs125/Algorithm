def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    if hp >= 0:
        for i in ant:
            count = hp // i
            answer += count
            hp -= count * i
    
    return answer