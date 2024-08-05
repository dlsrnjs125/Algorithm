def solution(s):
    answer = False
    pcnt = 0
    ycnt = 0
    
    pcnt += s.count('p')
    pcnt += s.count('P')
    ycnt += s.count('y')
    ycnt += s.count('Y')
    
    if pcnt == ycnt :
        answer = True

    return answer