def solution(myString):
    answer = []
    
    s = myString.split('x')
    for i in s:
        answer.append(len(i))
    return answer