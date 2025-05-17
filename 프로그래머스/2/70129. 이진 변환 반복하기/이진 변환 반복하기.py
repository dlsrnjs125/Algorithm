def solution(s):
    answer = []
    cnt = 0
    zeroCnt = 0
    
    while(True):
        if s == "1":
            break;
        
        zeroCnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        
        cnt += 1
    
    answer = [cnt, zeroCnt]
            
    return answer