def solution(array):
    answer = 0
    maxcount = 0
    set_array = set(array)
    
    for i in set_array:
        count = array.count(i)
        if maxcount < count:
            maxcount = count
            answer = i
        elif maxcount == count:
            answer = -1
    return answer