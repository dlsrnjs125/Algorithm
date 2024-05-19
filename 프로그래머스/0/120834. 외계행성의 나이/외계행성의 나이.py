def solution(age):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    for i in str(age):
        answer += alphabet[int(i)]
    return answer