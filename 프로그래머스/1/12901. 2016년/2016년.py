def solution(a, b):
    answer = ''
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month_len=[31,29,31,30,31,30,31,31,30,31,30,31]
    total_day=0
    
    for i in range(a-1):
        total_day+=month_len[i]
    total_day+=b
    result=total_day%7
    answer=day[result]
    
    return answer