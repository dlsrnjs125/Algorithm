def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
    
    answer = int(odd) + int(even)
    
    return answer