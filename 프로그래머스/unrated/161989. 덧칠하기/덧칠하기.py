def solution(n, m, section):
    answer = 0
    paint = section[0] - 1
    
    for i in section:
        if paint < i:
            paint = i + m - 1
            answer += 1
    
    return answer