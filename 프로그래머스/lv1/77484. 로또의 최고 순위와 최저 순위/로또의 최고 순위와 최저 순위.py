def solution(lottos, win_nums):
    answer = []
    scores = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    correct_num = 0
    zero = 0
    
    for i in lottos:
        if i in win_nums:
            correct_num += 1
        if i == 0:
            zero += 1
    answer.append(scores[zero + correct_num])
    answer.append(scores[correct_num])
    
    return answer