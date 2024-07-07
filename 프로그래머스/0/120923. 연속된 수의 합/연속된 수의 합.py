def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    
    answer = [i+1+start_num for i in range(num)]
    return answer