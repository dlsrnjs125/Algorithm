def solution(sides):
    answer = 0
    mx = max(sides)
    mn = min(sides)
    
    for i in range(mx-mn + 1, mx + 1):
        answer += 1
    
    for j in range(mx + 1, mx+mn):
        answer += 1
    return answer