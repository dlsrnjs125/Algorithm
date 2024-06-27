def solution(i, j, k):
    answer = 0
    
    for i in range(i, j+1, 1):
        tmp = str(i).replace(str(k), 'a')
        answer += tmp.count('a')
    return answer