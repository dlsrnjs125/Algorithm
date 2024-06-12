def solution(dots):
    answer = 0
    x = dots[0][0]
    y = dots[0][1]
    
    for i, j in dots:
        if x != i and y != j:
            x -= i
            y -= j
            break
    
    answer = abs(x) * abs(y)
    return answer