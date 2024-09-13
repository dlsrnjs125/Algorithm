def solution(my_string, is_prefix):
    answer = 0
    
    if is_prefix in my_string[:len(is_prefix)]:
        answer = 1
        
    return answer