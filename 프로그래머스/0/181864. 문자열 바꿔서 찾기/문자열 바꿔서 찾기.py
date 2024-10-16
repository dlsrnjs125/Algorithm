def solution(myString, pat):
    answer = 0
    my_string = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    
    if pat in my_string:
        answer = 1
        
    
    return answer