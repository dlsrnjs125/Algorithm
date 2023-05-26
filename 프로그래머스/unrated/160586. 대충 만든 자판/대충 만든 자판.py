def solution(keymap, targets):
    answer = []
    keys = []
    min_keys = dict()
    
    # 알파벳 버튼 수 구하기
    for k in keymap:
        key = dict()
        for i, val in enumerate(k):
            if val not in key:
                key[val] = i
        keys.append(key)

    # 각 알파벳의 최소 버튼 수 구하기
    for i in keys:
        for key, value in i.items():
            if key in min_keys:
                min_keys[key] = min(value, min_keys[key])
            else:
                min_keys[key] = value        
    
    for target in targets:
        cnt = 0
        for t in target:
            if t in min_keys:
                cnt += min_keys[t] + 1
            else: # 존재하지 않을 경우 -1 return
                cnt = -1
                break
        answer.append(cnt)
        
    return answer