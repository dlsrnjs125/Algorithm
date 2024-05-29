def solution(array, n):
    array.sort()
    answer = array[0]
    min_num = abs(n - array[0])
    
    for i in array:
        if min_num > abs(n-i):
            min_num = abs(n-i)
            answer = i
    
    return answer