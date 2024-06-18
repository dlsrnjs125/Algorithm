def solution(spell, dic):
    answer = 0
    
    for i in dic:
        if sorted(spell) == sorted(i):
            answer = 1
            break
        else:
            answer = 2
    return answer