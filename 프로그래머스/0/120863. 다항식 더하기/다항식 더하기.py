def solution(polynomial):
    answer = ''
    poly = polynomial.replace(' ', '').split('+')
    numx, num = 0, 0
    
    for i in poly:
        if i[-1] == 'x':
            if i[:-1]:
                numx += int(i[:-1])
            else:
                numx += 1
        else:
            num += int(i)
    
    if numx == 0:
        answer = str(num)
    elif numx == 1:
        if num == 0:
            answer = 'x'
        else:
            answer = 'x + ' + str(num)
    else:
        if num == 0:
            answer = str(numx) + 'x'
        else:
            answer = str(numx) + 'x + ' + str(num)
    
    return answer