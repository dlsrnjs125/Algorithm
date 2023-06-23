def solution(participant, completion):
    answer = ''
    p_dict = {i : 0 for i in participant}
    
    # 동명이인(중복) 확인
    for i in participant:
        p_dict[i] += 1
    
    # 완주자 제거
    for j in completion:
        p_dict[j] -= 1
    
    for k in p_dict:
        if p_dict[k] != 0:
            answer = k

    return answer