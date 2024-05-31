def solution(cipher, code):
    answer = ''
    tmp = 0
    
    for i in cipher:
        tmp += 1
        if tmp % code == 0:
            answer += i
    return answer