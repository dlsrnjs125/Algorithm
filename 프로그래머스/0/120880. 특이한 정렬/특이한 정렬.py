def solution(numlist, n):
    answer = []
    numlist = sorted(numlist, reverse=True)
    
    answer = sorted(numlist, key = lambda x : abs(n-x))
    return answer