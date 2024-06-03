def solution(s):
    answer = ''
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(i) == 1:
            answer += i
    return answer