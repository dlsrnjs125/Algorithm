def solution(bin1, bin2):
    answer = ''
    a = int(bin1, 2)
    b = int(bin2, 2)
    
    answer = bin(a + b).replace("0b", '')
    
    return answer