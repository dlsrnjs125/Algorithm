def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        li = []  # 쿼리 범위 내에서만 초기화
        
        for i in range(s, e+1):
            if arr[i] > k:
                li.append(arr[i])
        
        if li:  # li가 비어있지 않으면
            answer.append(min(li))
        else:  # li가 비어있으면 (=k보다 큰 요소가 없으면)
            answer.append(-1)
    
    
    return answer