def solution(strings, n):
    answer = []
    
    for i in strings:
        answer.append(i)
    answer.sort()
    
    answer = sorted(answer, key=lambda x:x[n])
    return answer