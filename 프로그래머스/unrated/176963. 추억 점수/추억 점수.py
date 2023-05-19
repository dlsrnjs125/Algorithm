def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        result = 0
        for j in i:
            if j in name:
                result += yearning[name.index(j)]
        answer.append(result)
    return answer