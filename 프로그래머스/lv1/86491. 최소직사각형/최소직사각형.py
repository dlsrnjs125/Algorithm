def solution(sizes):
    answer = 0
    x = []
    y = []
    
    for i in range(len(sizes)):
        x.append(max(sizes[i]))
        y.append(min(sizes[i]))
    answer = max(x) * max(y)
        
    return answer