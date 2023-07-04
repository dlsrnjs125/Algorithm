def solution(targets):
    cnt = 0
    shoot = -1 # targets가 0부터 시작하기 때문(개구간)
    targets.sort(key = lambda x: x[1])
    
    for i in targets:
        if i[0] > shoot:
            cnt += 1
            shoot = i[1] - 0.5 # 개구간이기때문에
    
    return cnt