def solution(my_string):
    answer = 0
    s = ''
    
    for i in my_string:
        if i.isdigit():
            s += (i)
        else:
            s += (' ')
    
    for j in s.split():
        answer += int(j)
    
    
    return answer