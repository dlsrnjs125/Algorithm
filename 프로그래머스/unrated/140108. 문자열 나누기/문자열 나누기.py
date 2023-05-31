def solution(s):
    answer = 0
    cnt1, cnt2 = 0, 0
    
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            alphbet = i # 첫 문자열 저장
        
        if alphbet == i:
            cnt1 += 1
        else:
            cnt2 += 1
    
    return answer