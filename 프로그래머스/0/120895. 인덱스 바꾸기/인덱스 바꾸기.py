def solution(my_string, num1, num2):
    answer = ''
    temp = my_string[num1]
    
    for index, i in enumerate(my_string):
        if index == num1:
            answer += my_string[num2]
        elif index == num2:
            answer += temp
        else:
            answer += i
        
    return answer