def solution(num_list, n):
    answer = []
    
    for idx, i in enumerate(num_list):
        if idx % n == 0:
            answer.append(i)
        
    return answer