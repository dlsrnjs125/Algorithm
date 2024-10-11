def solution(arr, n):
    answer = []
    
    if len(arr) % 2 == 0:
        for idx, i in enumerate(arr):
            if idx % 2 != 0:
                answer.append(i+n)
            else:
                answer.append(i)
    else:
        for idx, i in enumerate(arr):
            if idx % 2 == 0:
                answer.append(i+n)
            else:
                answer.append(i)
    return answer