def solution(answers):
    answer = []
    math1 = [1, 2, 3, 4, 5]
    math2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    
    for i in enumerate(answers):
        if i[1] == math1[i[0] % len(math1)]:
            scores[0] += 1
        if i[1] == math2[i[0] % len(math2)]:
            scores[1] += 1
        if i[1] == math3[i[0] % len(math3)]:
            scores[2] += 1
    for i in enumerate(scores):
        if i[1] == max(scores):
            answer.append(i[0] + 1)
    
    return answer