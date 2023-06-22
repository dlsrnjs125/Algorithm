def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, j in enumerate(num):
        s = s.replace(j, str(i))
    return int(s)