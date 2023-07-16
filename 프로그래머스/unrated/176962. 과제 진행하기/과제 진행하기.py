def timer(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []
    stack = []
    
    # 시간을 int값으로 계산하기 편하게 변경
    for plan in plans:
        plan[1], plan[2] = timer(plan[1]), int(plan[2])
    
    plans.sort(key=lambda x : x[1]) # 시작시간을 기준으로 정렬

    t, idx = plans[0][1], 0
    while idx < len(plans):
        stack.append(plans[idx]) # 첫번째 숙제 넣기
        if t < stack[-1][1]: # 잠시 멈춘 과제 -> 나중에 들어온 과제부터 실행
            t = stack[-1][1]
        
        while stack and stack[-1][2]:
            t += 1
            stack[-1][2] -= 1
            if not stack[-1][2]: # 과제 남은 시간이 -> 0
                answer.append(stack.pop()[0])
            if idx+1 < len(plans) and t == plans[idx+1][1]: # 과제 시작시간에 맞춰서 진행중인 과제로 만들기
                stack.append(plans[idx+1])
                idx += 1
        idx += 1
    
    return answer