def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    
    for idx, i in enumerate(num_list):
        if idx % 2 == 0:
            odd += i
        else:
            even += i
    
    answer = max(odd, even)
    
    return answer