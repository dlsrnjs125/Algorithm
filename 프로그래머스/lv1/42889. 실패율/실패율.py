def solution(N, stages):
    answer = {}
    total_stages = len(stages)
    
    for stage in range(1, N+1):
        if total_stages != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt / total_stages
            total_stages -= cnt
        else:
            answer[stage] = 0
    answer = sorted(answer, key=lambda x : answer[x], reverse=True)
    
    return answer