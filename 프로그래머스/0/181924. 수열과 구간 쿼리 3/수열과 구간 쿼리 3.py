def solution(arr, queries):
    answer = []
    
    for i in queries:
        tmp = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = tmp
        
    answer = arr
    return answer