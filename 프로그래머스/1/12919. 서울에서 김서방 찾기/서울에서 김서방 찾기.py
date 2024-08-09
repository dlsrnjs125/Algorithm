def solution(seoul):
    answer = ''
    for idx, i in enumerate(seoul):
        if i == "Kim":
            answer = '김서방은 ' + str(idx) + '에 있다'
    return answer