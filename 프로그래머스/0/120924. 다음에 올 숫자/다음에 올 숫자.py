def solution(common):
    answer = 0
    one, two, three = common[:3]
    if two - one == three - two:
        answer = common[-1] + (two-one)
    elif two // one == three // two:
        answer = common[-1] * (two//one)
    return answer