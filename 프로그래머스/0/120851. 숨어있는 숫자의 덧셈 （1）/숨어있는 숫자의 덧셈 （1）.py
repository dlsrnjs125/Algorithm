def solution(my_string):
    answer = 0
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    for i in my_string:
        if i in numbers:
            answer += int(i)
    return answer