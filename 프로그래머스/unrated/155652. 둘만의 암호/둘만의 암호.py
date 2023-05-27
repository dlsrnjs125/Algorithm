def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for ch in skip: # ch => skip의 문자 하나하나
        if ch in alphabet:
            alphabet = alphabet.replace(ch, "") # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        change = alphabet[(alphabet.index(i) + index) % len(alphabet)]
        answer += change
            
    return answer