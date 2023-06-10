def solution(X, Y):
    answer = ''
    
    # 0 ~ 9까지의 반복되는 숫자 개수 세기
    numX = {str(n) : 0 for n in range(10)}
    numY = {str(n) : 0 for n in range(10)}
    
    for x in X:
        numX[x] += 1
    
    for y in Y:
        numY[y] += 1
    
    # sort를 안하고 가장 큰 수 만들기
    for i in range(9, -1, -1):
        i = str(i)
        num = min(numX[i], numY[i])
        
        answer = ''.join([answer, i*num])
    
    if answer == '': # 짝궁 존재 X
        return "-1"
    elif len(answer) == answer.count('0'): # 공통 숫자가 0으로만 구성된 경우
        return '0'
    else:
        return answer