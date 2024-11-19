def solution(num_list):
    answer = 0
    cnt = 0
    
    for i in num_list:
        cnt = 0
        while i != 1:
            cnt += 1
            if i % 2 == 0:
                i = i / 2
            else:
                i = (i - 1) / 2
        answer += cnt
    
    return answer