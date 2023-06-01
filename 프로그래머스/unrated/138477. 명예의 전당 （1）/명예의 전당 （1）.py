def solution(k, score):
    answer = []
    rank = []
    
    for i in score:
        rank.append(i)
        rank.sort(reverse=False)
        
        # 최하위 점수 만들기
        if len(rank) > k:
            del rank[0]
            
        answer.append(rank[0])
        
    return answer