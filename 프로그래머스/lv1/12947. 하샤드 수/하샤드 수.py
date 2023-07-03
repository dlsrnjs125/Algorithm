def solution(x):
    answer = True
    nums = str(x)
    sum = 0
    
    for i in nums:
        sum += int(i)
        
    if x % sum != 0:
        answer = False
    
    return answer