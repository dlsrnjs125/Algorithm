def solution(strArr):
    answer = 0
    a = [0] * 31
    for i in strArr:
        a[len(i)] += 1
        
    answer = max(a)
    
    return answer