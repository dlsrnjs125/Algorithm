def solution(my_string):
    answer = ''
    my_string = sorted(my_string.lower())
    
    for i in range(len(my_string)):
        answer += my_string[i]
    return answer