def solution(array, commands):
    answer = []
    
    for i in commands:
        arrays = []
        for j in range(i[0] -1, i[1]):
            arrays.append(array[j])
        arrays.sort()
        answer.append(arrays[i[2] - 1])
    return answer