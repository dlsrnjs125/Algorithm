import re
def solution(dartResult):
    answer = 0
    
    darts = re.findall("([0-9]+)([SDT])([*#]?)", dartResult)
    answer = [0] * len(darts)
    
    for idx, (num, mul, op) in enumerate(darts):
        answer[idx] = int(num)

        if mul == 'D':
            answer[idx] **= 2
        elif mul == 'T':
            answer[idx] **= 3

        if op == '*':
            answer[idx] *= 2
            if 0 <= idx - 1:
                answer[idx - 1] *= 2
        elif op == '#':
            answer[idx] *= -1
            
    return sum(answer)