def solution(numbers, k):
    answer = 0
    n = (2*(k-1)) % len(numbers)
    answer = numbers[n]
            
    return answer