def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse=True) # 내림차순 정리
    
    for i in emergency:
        answer.append(tmp.index(i)+1)
    
    return answer