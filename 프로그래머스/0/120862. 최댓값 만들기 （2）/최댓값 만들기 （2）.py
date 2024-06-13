def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers[0] * numbers[1]
    b =  numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
    
    if a > b:
        answer = a
    else:
        answer = b
    return answer