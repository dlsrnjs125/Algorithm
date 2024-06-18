def solution(spell, dic):
    answer = 0
    spell = sorted(spell)
    
    for i in dic:
        if spell == sorted(i):
            answer = 1
            break
        else:
            answer = 2
    return answer