def solution(num, k):
    answer = 0
    for idx, i in enumerate(str(num)):
        if int(i) == k:
            answer = idx+1
            break
        else:
            answer = -1
    return answer