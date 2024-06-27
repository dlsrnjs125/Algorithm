def solution(before, after):
    answer = 1
    
    for i in after:
        if i not in before:
            answer = 0
        else:
            before = before.replace(i, '',1)
            
    return answer