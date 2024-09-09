def solution(num_list):
    answer = -1
    
    for idx, i in enumerate(num_list):
        if i < 0:
            answer = idx
            break
        
    return answer