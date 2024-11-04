def solution(number):
    answer = 0
    nSum = 0
    
    for i in number:
        nSum += int(i)
    
    answer = nSum % 9
    return answer