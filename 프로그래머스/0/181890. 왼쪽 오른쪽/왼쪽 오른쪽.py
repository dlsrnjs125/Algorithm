def solution(str_list):
    answer = []
    
    for idx, i in enumerate(str_list):
        if i == 'l':
            return str_list[:idx]
        if i == 'r':
            return str_list[idx+1:]
        
    return answer