def solution(my_string):
    answer = ''
    string = []
    
    for i in my_string:
        if i not in string:
            string.append(i)
            answer += i
        else:
            continue
    
    return answer