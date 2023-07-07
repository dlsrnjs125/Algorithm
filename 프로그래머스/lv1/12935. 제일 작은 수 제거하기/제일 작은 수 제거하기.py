def solution(arr):
    answer = []
    min_arr = min(arr)
    
    for i in arr:
        if i != min_arr:
            answer.append(i)
    
    if len(arr) == 1:
        answer.append(-1)

    
    return answer