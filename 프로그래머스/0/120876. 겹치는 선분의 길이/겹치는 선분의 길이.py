def solution(lines):
    answer = 0
    line1 = set(i for i in range(lines[0][0], lines[0][1]))
    line2 = set(i for i in range(lines[1][0], lines[1][1]))
    line3 = set(i for i in range(lines[2][0], lines[2][1]))
    
    answer = len(set(line1 & line2 | line1 & line3 | line2 & line3))
    
    
    return answer